#list s3 objects using boto3
import boto3
s3_resource=boto3.client("s3")
objects=s3_resource.list_objects(Bucket="jgree09")["Contents"]
len(objects)
if len(objects)>0:
    print("object exists")
for objects in objects:
    print(object)