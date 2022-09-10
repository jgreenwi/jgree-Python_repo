#How to delete objects from s3 using boto
import boto3
s3_resource=boto3.client("s3")
s3_resource.client.delete_object(
    Bucket='jgree09'
    key ="unsplash.jpg"
    )
print(response)
#delete multiple objects
import os 
import glob

#find all the obj from the bucket
objects=s3_resource.list_objects(Bucket="jgree09")["Contents"]
len(objects)

#automation code
for object in objects:  
    s3_resource.delete_object(Bucket="jgree09" ,
    key=object["Key"])
    print(object["Key"])