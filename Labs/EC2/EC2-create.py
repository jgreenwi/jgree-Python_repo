#create EC2 using boto3
import boto3
#create resource
ec2_resource=boto3.resource("ec2")
ec2_resource.create_instances(ImageId='ami-05fa00d4c63e32376',
    InstanceType='t2.micro',
    MaxCount=1,
    MinCount=1)

#automation code
[ec2.Instance(id='ami-05fa00d4c63e32376')]
