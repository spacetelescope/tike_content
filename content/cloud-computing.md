
# Introduction to Data Management on AWS
If you are planning on accessing or producing a lot of data (more than a couple Gigabytes), it is worth paying attention to where the data is coming from and how to write your results.  TESS and Kepler data are available through Amazon's public S3 buckets (Amazon's name for it's file store system).  If retrieved from those buckets, you can achieve significant speed up over retrieving the data from the MAST.  These tutorials will teach you how to make better use of this cloud environment and some of the services AWS has to offer

- Intro to AWS: credentials and costs
- Intro to AWS: Public Data in the Cloud: [Accessing cloud data with astroquery](./code/cloud_astroquery.ipynb)
- Intro to AWS: Writing data to S3 buckets as part of your workflow
- TESScut in the cloud
- Community software in the cloud: Lightkurve and eleanor


# Optimization
Working on AWS is not exactly the same as working on your laptop. It provides access to high power machines and an almost local archive of mission data. However, it involves learning data handling using the S3 buckets and boto3.  What follows are tutorials and links to help you get started with using cloud-hosted data and computers.


- Dask: [Paralellize a Periodogram](./code/Dask_meanFTloop.ipynb)
- Optimizing your code in the cloud
- Spinning up your own EC2 instance

