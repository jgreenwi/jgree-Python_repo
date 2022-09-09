#AWS automation using boto3: How to upload a file to s3
import boto3
s3_resource=boto3.client("s3")
s3_resource.upload_file(
    Filename="unsplash.jpg",
    Bucket="jgree09",
    Key="unsplash.jpg"
    )
    
import os
import glob

cwd=os.getcwd()
cwd=cwd+"/upload/"
file=glob.glob(cwd+"*.png")
#automation code:
for file in files:
    s3_resource=boto3.client("s3")
    s3_resource.upload_file(
    Filename=file,
    Bucket="jgree09",
    Key=file.split("/")(-1)
    )
files[0].split("/")(-1)
#the above command list files and presents the last item