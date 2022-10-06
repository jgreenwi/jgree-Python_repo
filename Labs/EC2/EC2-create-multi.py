#create multiple EC2 using boto3
import boto3
    ec2_resource=boto3.resource("ec2")
    ec2_resource.create_instances(ImageId='',
        InstanceType='t2.micro',
        MaxCount=3,
        MinCount=3
        )
        