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

