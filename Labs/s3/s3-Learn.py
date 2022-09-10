#Create S3 Bucket Using Python Boto3
#Pre req to install using your terminal:
    #pip install boto3
    #pip3 instal awscli
#create iam user 
    #user needs programmatic access
    #permission=admin access policy
#configure your aws cli with iam user credentials
#Create s3 bucket commands:
import boto3
aws_resource=boto3.resource('s3') #creates a variable within s3
bucket=aws_resource.Bucket('jgree09') #names your bucket
response = bucket.create(
    ACL='public-read'
        
)  

print(response)

#this Automation will show you how to Search s3 Buckets using Python Boto3
#pre-reqs are the same as above 
#Tutorial Search Bucket 
import boto3 
resource=boto3.resource('s3')
bucket_list=list(resource.buckets.all())
len(bucket_list)
for bucket in resource.buckets.all():
    print(bucket.name)

#AWS s3 automation using boto3 
#How to get a s3 bucket creation date using boto3
import boto3
s3_resource=boto3.client("s3")
s3_resource.list_buckets()["Buckets"][0]["Name"]
#s3_resource.list_buckets()["Buckets"][0]["Creationdate"]
creation_date=s3_resource.list_buckets()["Buckets"][0]["CreationDate"]
creation_date.strftime("%d%m%y_%H:%M:%s")
