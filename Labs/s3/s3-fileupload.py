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
for file in file:
    s3_resource=boto3.client("s3")
    s3_resource.upload_file(
    Filename=file,
    Bucket="jgree09",
    Key=file.split("/")(-1)
    )
#file[0].split("/")(-1)
#the above command list files and presents the last item

#important notes:
#in order to upload a file using an IDE you must first save it to the IDE to upload it into your code. Otherwise you will receve an error messages "no file"