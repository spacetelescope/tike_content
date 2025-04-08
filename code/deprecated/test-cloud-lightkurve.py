#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 19:31:11 2020

@author: smullally
"""

from astroquery.mast import Observations

Observations.enable_cloud_dataset(provider='AWS')

target = "Kepler-10"

#Do a cone search and find the Kepler long cadence data for your target
obs = Observations.query_object(target,radius="0s")
want = (obs['obs_collection'] == "Kepler") & (obs['t_exptime'] ==1800.0)

#Pick which data you want to retrieve
data_prod = Observations.get_product_list(obs[want])
filt_prod = Observations.filter_products(data_prod, description="Lightcurve Long Cadence (CLC) - Q4")

#Move data from the S3 bucket to the default astroquery location. 
#cloud_only=True means that data will only be retrieved if available on AWS S3
manifest = Observations.download_products(filt_prod)

#%%
import pdb

from lightkurve import search_targetpixelfile

def afunction():
    
    pdb.set_trace()

    pixelfile = search_targetpixelfile("KIC 8462852", quarter=16).download();