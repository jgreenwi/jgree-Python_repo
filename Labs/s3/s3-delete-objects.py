#How to delete objects from s3 using boto
import boto3
s3_resource=boto3.client("s3")
s3_resource.client.delete_object(
    Bucket='jgree09'
    Key="unsplash.jpg"
    )