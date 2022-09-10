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
#code for checking amt of vpc
x=client.describe_vpcs()
no_of_vpcs=x["Vpcs"]
len(no_of_vpcs)
#automation #2
for vpc in no_of_vpcs:
    print(vpc["vpc-04c098223e51ee806"])