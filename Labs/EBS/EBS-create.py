#Create EBS Volume Snapshot
import boto3
ec2_client=boto3.client("ec2")
ec2_client.create_snapshot( Description='snapshot from basevolume using python',
    VolumeId='vol-0ae7b90affee6d9f1')

ec2_client=boto3.client("ec2")
ec2_client.create_volume(AvailabilityZone='us-east-1a',
    Encrypted=True,
    Size=12,
    SnapshotID='snap-08391e1d0fe151035',
    VolumeType='gp2')