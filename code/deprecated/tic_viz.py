#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 09:17:15 2020

@author: smullally
"""


from astroquery.mast import Catalogs
import panel as pn
import pandas as p
from io import StringIO
import numpy as np
from astroquery.mast import Observations
from astroquery.mast import Tesscut
from astropy.coordinates import SkyCoord
from astropy.wcs import WCS
from astropy.io import fits
import matplotlib.pyplot as plt
from astropy.table import QTable
import re

def query_tic(name = "TIC 261136679"):
    """
    Creates a set of widgets to view and filter the TIC after doing a cone
    serach around a target of interest. Target can be entered after running,
    or as part of executing this function.
    
    Once the table is filtered, it can write a CSV file. This can only be done 
    
    
    Input:
        name (optional) -- String -- Star name or coordiantes
    
    """
    optcols = ['pmRA','pmDEC','Tmag','objType','typeSrc','version','HIP','TYC','UCAC','TWOMASS','SDSS','ALLWISE',\
 'GAIA','APASS','KIC','POSflag','e_pmRA','e_pmDEC','gallong','gallat','Bmag','e_Bmag','Vmag','e_Vmag','umag','e_umag',\
 'Jmag','e_Jmag','Hmag','e_Hmag','Kmag','e_Kmag','TWOMflag','GAIAmag','e_GAIAmag','e_Tmag','TESSflag','e_Teff',\
 'e_logg','MH','e_MH', 'gaiaqflag','starchareFlag','dstArcSec']
    
    starname = pn.widgets.TextInput(name="Star Name or Coordinates", value = name)
    distsearch = pn.widgets.FloatSlider(name='Radial Distance from Star (arcmin)', start = 0, end = 12, 
                                   value = 3, step = .1)
    magfilt = pn.widgets.FloatSlider(name='TESS Magnitude Limit', start=0, end=25, value = 15, step = 0.5 )
    colchoice = pn.widgets.MultiChoice(name="Choose Extra Columns", options=optcols)

    

    @pn.depends(starname, distsearch, colchoice, magfilt)
    def quick_tic_query(starname, distsearch, colchoice, magfilt):

        req_cols = ['ID', 'Tmag','Teff','logg','ra', 'dec','dstArcSec']
        cols = req_cols + colchoice
        catalogData = tic_cone_search(star_name=starname, radius_deg = distsearch/60)
        want = catalogData['Tmag'] <= magfilt
        return(catalogData[want][cols].show_in_notebook(display_length=5))
    
    @pn.depends(starname, distsearch, colchoice, magfilt)
    def filtered_file(starname, distsearch, colchoice, magfilt):

        req_cols = ['ID', 'Tmag','Teff','logg','ra', 'dec','dstArcSec']
        cols = req_cols + colchoice
        catalogData = tic_cone_search(star_name=starname, radius_deg = distsearch/60)
        want = catalogData['Tmag'] <= magfilt
        sio = StringIO()
        df = catalogData[want][cols].to_pandas()
        print(catalogData[want][cols])
        df.to_csv(sio)
        sio.seek(0)
        return(sio)    
    
    filedownload = pn.widgets.FileDownload(callback=filtered_file, filename='filtered_tic.csv', embed=False)
    
    row = pn.Row(starname, filedownload)
    mypanel = pn.Column(row, distsearch, magfilt, colchoice, quick_tic_query)

    return(mypanel)

def tic_cone_search(star_name="Kepler-10", radius_deg = .2):
    catalogData = Catalogs.query_object(star_name, radius = radius_deg, catalog = "TIC")
    
    return catalogData


#---
#For DV/TIC/Observation/overlay visualization

def target_overview(name = "pi men", radius_deg = 0.12, num_search = 10):
    
    catalogData = tic_cone_search(star_name = name, radius_deg = radius_deg)
    print("Retrieved TIC Data")
    image, wcs = get_ffi_image(catalogData[0], cutout_deg=radius_deg)
    print("Retrieved TESS Image")
    ts_table, dv_table = get_twomin_obs(catalogData['ID'][0:num_search])

    
    magrange = pn.widgets.RangeSlider(name='Magnitude Range', start=1, end=25, value = (4,15), step = 0.1 )
    distrange = pn.widgets.RangeSlider(name='Radial Distance from Star (arcmin)', start = 0, end = radius_deg*60, 
                                       value = (0,radius_deg*60), step = .1)
    teffrange = pn.widgets.RangeSlider(name='Effective Temperature (K)', start = 0, end = 10000, 
                                       value = (0,10000), step = 50)
    colchoice = pn.widgets.MultiChoice(name="Choose Extra Columns", options=list(catalogData.colnames))
    
    
    @pn.depends(magrange, distrange, teffrange, colchoice)
    def react_filter_tic(magrange, distrange, teffrange, colchoice, ts=ts_table, dv=dv_table,\
                         data = catalogData, image = image, wcs=wcs, disp_num = 15):
        t = filter_tic_data(data, mags=magrange, dist=distrange, teff=teffrange,
                       opt_cols=colchoice)
        Table = t.show_in_notebook(display_length=disp_num)
        
        fig = plot_image_targetlist(t, image, wcs, nearest=len(t), fsize=(10,10))
        
        lc_table = ts.show_in_notebook(display_length=disp_num)
        search_table = dv.show_in_notebook(display_length=disp_num)
                                   
        return pn.Tabs(
                ('TIC Table', Table),
                ('LC Data Table', lc_table),
                ('DV Data Table', search_table),
                ('Plot', pn.pane.plot.Matplotlib(fig))
                        )                          
        #return(t.show_in_notebook(display_length=15))
    
    widgets  = pn.Column("<br>\n# TESS Overview ", colchoice, magrange, distrange, teffrange, react_filter_tic)
    mypanel = pn.Row(widgets)
    
    return(mypanel)
    
def filter_tic_data(catalogData, mags=[1,25], dist = (0, 1), teff = (1000,10000),
                   opt_cols=[ 'Jmag','TWOMASS']):
    req_cols = ['ID', 'Tmag','Teff','logg','ra', 'dec','dstArcSec']
    
    cols = req_cols + opt_cols
    wantteff = ((catalogData['Teff']> teff[0]) & (catalogData['Teff']<= teff[1])) | np.isnan(catalogData['Teff'])
    wantmag = (catalogData['Tmag'] <= mags[1]) & (catalogData['Tmag'] >= mags[0])
    wantdist = (catalogData['dstArcSec'] <= dist[1]*60) & \
                    (catalogData['dstArcSec'] >= dist[0]*60)
    want = wantmag & wantdist & wantteff

    return catalogData[want][cols]

    
def get_twomin_obs(ticlist):
    """
    Given a list of ticids, return a table of all the data that is available on that target.
    The table will be well formated to just be one one describing 
    the available sectors per target.
    
    Input: list of ticids, int
    Return: full table (astropy table of tic, obsid, filenames, camera, ccd)
            for all relevant two minute data files.
            summary table (one line per ticid), list of sectors, list of camera and ccd
    """
    
    sectors = []
    gis = []
    obsid = []
    tmin = []
    tmax = []
    exptime = []
    target = []
    
    dv_sectors = []
    dv_obsid = []
    dv_tmin = []
    dv_tmax = []
    dv_target = []
    dv_exptime = []
    
    for tic in ticlist:
        observations = Observations.query_criteria(obs_collection = "TESS",
                                             dataproduct_type = ["timeseries"],
                                             target_name = tic)
        if len(observations) > 0:
            observations.sort(keys=['sequence_number', 'target_name'])
            
            for obs in observations:
                #Match for multi-sector observations
                match = re.search("s\d\d\d\d-s\d\d\d\d",obs['obs_id'])
                
                if match == None:
                
                    if int(obs['target_name']) == int(tic):
                        obsid.append(obs['obs_id'])
                        gis.append(obs['proposal_id'])
                        sectors.append(obs['sequence_number'])
                        tmin.append(obs['t_min'])
                        tmax.append(obs['t_max'])
                        exptime.append(int(obs['t_exptime']/60.0))
                        target.append(obs['target_name'])
                    
                else:
                    dv_sectors.append(match.group(0))
                    dv_obsid.append(obs['obs_id'])
                    dv_tmin.append(obs['t_min'])
                    dv_tmax.append(obs['t_max'])
                    dv_target.append(obs['target_name'])
                    dv_exptime.append(int(obs['t_exptime']/60.0))
    
    ts_table = QTable([target, sectors, gis, obsid, exptime, tmin,tmax],
                 names=('target_tic', 'sectors', 'GI_nums', 'obs_id', 'Exp_time_min','t_min','t_max'),
                 meta={'name':'observation table'})
    dv_table = QTable([dv_target, dv_sectors, dv_obsid, dv_exptime, dv_tmin, dv_tmax],
                 names=('target_tic', 'sector_range','obs_id', 'Exp_time_min','t_min','t_max'),
                 meta={'name':'Multi-Sector Planet Search'})
    
    return ts_table, dv_table


def plot_cutout(image):
    """
    Plot image and add grid lines.
    """
    
    #fig = plt.figure
    plt.imshow(image, origin = 'lower', cmap = plt.cm.YlGnBu_r, 
           vmax = np.percentile(image, 91),
           vmin = np.percentile(image, 5))

    plt.grid(axis = 'both',color = 'white', ls = 'solid')
    


def get_ffi_image(target, cutout_deg = 0.1):
    
    ra = target['ra']
    dec = target['dec']
    
    coord = SkyCoord(ra, dec, unit = "deg")
    print(coord)
    
    npixels = 2*np.ceil(cutout_deg*3600/21) + 4 #This assumes 21arcsecond pixels)
    
    
    if npixels > 60:
        npixels = 60
        print("Warning: cutout size set to 80 pixels.")
    if npixels < 10:
        npixels = 10
        
    sector_tab = Tesscut.get_sectors(coordinates=coord)
    
    try:
        hdulist = Tesscut.get_cutouts(coord, size = npixels, sector = sector_tab[0]['sector'])
    except:
        print("Cutout not available")
        return [[0][0]], "no wcs"
    
    hdu = hdulist[0]
    aveImage = (hdu[1].data['FLUX'][0] + hdu[1].data['FLUX'][1] + hdu[1].data['FLUX'][2])/3

    wcs = WCS(hdu[2].header)
    
    return aveImage, wcs
    
def plot_image_targetlist(targetlist, image, wcs, nearest=15, fsize=(6,6)):
    
    fig = plt.figure(figsize = fsize)
    fig.add_subplot(111, projection = wcs)
    plot_cutout(image)

    plt.xlabel('RA', fontsize = 12)
    plt.ylabel('Dec', fontsize = 12)
    
    ra = targetlist[0]['ra']
    dec = targetlist[0]['dec']

    #Plot the first star
    starloc = wcs.all_world2pix([[ra,dec]],0) 
    plt.scatter(starloc[0,0], starloc[0,1],s = 45,color = 'red')

    # Make it a list of Ra, Dec pairs of the bright ones. 
    nearby_stars = list( map( lambda x,y:[x,y], targetlist['ra'], targetlist['dec'] ) )
    
    # Plot nearby stars 
    nearby_loc = wcs.all_world2pix(nearby_stars[1:nearest],0)
    plt.scatter(nearby_loc[0:nearest, 0], nearby_loc[0:nearest, 1], 
                s = 25, color = 'orange')
    
    for i,v in enumerate(nearby_loc[:nearest]):
        r = 2 * np.random.rand() - 1
        n = i+1 #first is the target, not plotted here
        plt.annotate(str(n), (nearby_loc[i][0], nearby_loc[i][1]),
                     textcoords="offset points", xytext=(r,r), ha='left',
                    color = 'red', fontsize=15)
    plt.title("TIC "+ str(targetlist[0]['ID']))
    
    return(fig)


    
