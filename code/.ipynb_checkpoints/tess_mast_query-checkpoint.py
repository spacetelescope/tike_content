import numpy as np
from astroquery.mast import Catalogs
from astroquery.mast import Observations
from astroquery.mast import Tesscut
from astropy.coordinates import SkyCoord
from astropy.wcs import WCS
from astropy.io import fits
import matplotlib.pyplot as plt
from astropy.table import QTable
import panel as pn
import re

def tic_cone_search(star_name="Kepler-10", radius_deg = .3):
    catalogData = Catalogs.query_object(star_name, radius = radius_deg, catalog = "TIC")
    
    return catalogData

def filter_tic_data(catalogData, mags=[1,25], dist = (0, 1), teff = (3000,6000),
                   opt_cols=[ 'Jmag','TWOMASS'], showdata=True):
    req_cols = ['ID', 'Tmag','Teff','logg','ra', 'dec','dstArcSec']
    cols = req_cols + opt_cols
    wantteff = (catalogData['Teff']> teff[0]) & (catalogData['Teff']<= teff[1])
    wantmag = (catalogData['Tmag'] <= mags[1]) & (catalogData['Tmag'] >= mags[0])
    wantdist = (catalogData['dstArcSec'] <= dist[1]*60) & \
                    (catalogData['dstArcSec'] >= dist[0]*60)
    want = wantmag & wantdist & wantteff
    
    #Show data with show_in_notebook, or just return filtered table.
    if showdata:
        t = catalogData[want][cols].show_in_notebook(display_length=15)

    
    return catalogData[want][cols]


def get_tic_info(star_name="TIC 1234647", radius_deg=.10, maglimit = 14.5, cols=['ID', 'Tmag', 'Jmag', 'Teff','logg','ra', 'dec','TWOMASS','dstArcSec']):
        
    catalogData = Catalogs.query_object(star_name, radius = radius_deg, catalog = "TIC")
    want = catalogData['Tmag'] <= maglimit
    #I always want the first two regardless of magnitude, it returns sorted by angular distance
    want[0:2] = [True, True]
    
    return(catalogData[want][cols])

# Define a function to simplify the plotting command that we do repeatedly.
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
    
#I'm not using this one below..it does too much all at oonce.
def overplot_ticffi(targetlist, cutout_deg = .1,nearest=10):
    """
    Plot tic positions on top of an ffi
    sector =0 means use the first available, otherwise use the specified sector.
    targetlist is a astropy table containing ID, ra, dec, Tmag
    The cutout will be performed around the first ra/dec
    """
    ra = targetlist[0]['ra']
    dec = targetlist[0]['dec']

    coord = SkyCoord(ra, dec, unit = "deg")
    
    npixels = 2*np.ceil(cutout_deg*3600/21) + 4 #This assumes 21arcsecond pixels)
    
    if npixels > 60:
        npixels = 60
        print("Warning: cutout size set to 80 pixels.")
    if npixels < 10:
        npixels = 10
    
    try:
        hdulist = Tesscut.get_cutouts(coord, size = npixels)
    except:
        print["Cutout not available"]
        return
    
    hdu = hdulist[0]
    firstImage = hdu[1].data['FLUX'][0]

    wcs = WCS(hdu[2].header)

    fig = plt.figure(figsize = (6, 6))
    fig.add_subplot(111, projection = wcs)
    plot_cutout(firstImage)

    plt.xlabel('RA', fontsize = 12)
    plt.ylabel('Dec', fontsize = 12)


    starloc = wcs.all_world2pix([[ra,dec]],0)  #Second is origin
    plt.scatter(starloc[0,0], starloc[0,1], s = 50, color = 'red')

    # Make it a list of Ra, Dec pairs of the bright ones. This is now a list of nearby bright stars.
    nearby_stars = list( map( lambda x,y:[x,y], targetlist['ra'], targetlist['dec'] ) )
    
    # Plot nearby stars as well, which we created using our Catalog call above.
    nearby_loc = wcs.all_world2pix(nearby_stars[1:nearest],0)
    plt.scatter(nearby_loc[1:nearest, 0], nearby_loc[1:nearest, 1], 
                s = 27, color = 'orange')
    
    for i, v in enumerate(nearby_loc[:nearest]):
        r = np.random.rand()
        n = i+1 #first is the target, not plotted here
        plt.annotate(str(n), (nearby_loc[i][0], nearby_loc[i][1]),
                     textcoords="offset points", xytext=(-.1+r,-.1+r), ha='left',
                    color = 'orange', fontsize=17)
    plt.title("TIC "+ str(targetlist[0]['ID']))
    
    return firstImage, wcs, fig

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

def run_tic_info(ticid, maglimit):

    size = .11
    nearest = 15
    cols = ['ID', 'Tmag', 'Jmag', 'Teff','logg','ra', 'dec','dstArcSec']
    
    ticinfo = get_tic_info(ticid, radius_deg = size, cols=cols)
    ticinfo.show_in_notebook(display_length=nearest)
    
    image, wcs = overplot_ticffi(ticinfo, cutout_deg = size, nearest=nearest)
    
    ticlist = ticinfo['ID']
    obs_table, dv_table = get_twomin_obs(ticlist[0:3])
    obs_table.show_in_notebook()
    
    return(ticinfo)
    
