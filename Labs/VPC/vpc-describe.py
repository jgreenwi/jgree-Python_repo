#describe VPC
import boto3
client=boto3.client("ec2")
client.describe_vpcs()
#automation code :
response = client.describe_vpcs(
    VpcIds=[
        'vpc-04c098223e51ee806',
    ],
  
)

