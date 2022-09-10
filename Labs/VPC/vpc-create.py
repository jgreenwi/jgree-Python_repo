#create VPC with boto3. Important* VPC's title is ec2
import boto3
client=boto3.client("ec2")
client.create_vpc(CidrBlock='10.0.0.0/16')
