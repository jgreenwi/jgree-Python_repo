#Delete EBS with boto 
import boto3
ec2_client=boto3.client("ec2")
ec2_client.delete_snapshot(SnapshotId='snap-0b73278eb29be66bc')

