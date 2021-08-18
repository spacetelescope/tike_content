# How to work with data in the cloud?

This page contains examples of how to work with data in the cloud.

#### How to configure astroquery or S3FS to read data products from AWS S3 buckets.

[MAST AWS Public Datasets](https://registry.opendata.aws/collab/stsci/) can be accessed using various client libraries, including Astroquery, boto3, S3FS, and others. These data are free to access and download: they do not require you to have an AWS account or use AWS credentials. Here we show a few very basic examples in Python:

1. Using [S3FS](https://s3fs.readthedocs.io/en/latest/)

```
import s3fs
fs = s3fs.S3FileSystem(anon=True) #initialize S3 filesystem object
fs.ls('s3://stpubdata/tess/public/',refresh=True) #list TESS data directory
#transfer a file from S3
f=fs.get('s3://stpubdata/tess/public/ffi/s0031/2020/294/4-1/tess2020294194027-s0031-vrow-4-1-c-0198-a_fast-col.fits','tess_test.fits')
```

2. Using [Astroquery](https://astroquery.readthedocs.io/en/latest/mast/mast.html)

```
from astroquery.mast import Observations

#Identify a few TESS Sector 10 FFI products
obsTable = Observations.query_criteria(obs_id=f"tess-s0010-4-1")
products = Observations.get_product_list(obsTable)
filtered = Observations.filter_products(products[0:10],
                                        productSubGroupDescription="FFIC",
                                        mrp_only=False)

#Return the AWS S3 locations (URIs)
Observations.enable_cloud_dataset(provider='AWS')
uris = Observations.get_cloud_uris(filtered)
print(uris[0])

#Download a few example products
manifest = Observations.download_products(products[0:2], cloud_only=True)
```

See example notebooks:
- [Intro to STScI Data in AWS.ipynb](../code/Intro%20to%20STScI%20Data%20in%20AWS.ipynb)
- [cloud_astroquery.ipynb](../code/cloud_astroquery.ipynb)
- [s3buckets_boto3.ipynb](../code/s3buckets_boto3.ipynb)

#### How to use create cutouts from TESS FFI data hosted in AWS.

Content in progress

#### How to read and write data to your own S3 bucket.

Content in progress
