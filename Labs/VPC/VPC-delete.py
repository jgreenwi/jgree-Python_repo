#delete VPC using boto3
import boto3
client=boto3.client("ec2")



#automation
response = client.delete_vpc(
    VpcId='vpc-04c098223e51ee806',
)

