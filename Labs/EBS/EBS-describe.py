#describe EBS with boto
import boto3
ec2_boto3=boto3.client("ec2")
ec2_boto3.describe_snapshots()
#automation code
ec2_boto3.describe_snapshots(SnaoshotIds=['snap-0b73278eb29be66bc'])