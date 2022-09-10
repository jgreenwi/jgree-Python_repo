#Terminate multiple EC2 instances using boto3
import boto3
ec2_client=boto3.client("ec2")
x=ec2_client.describe_instances()
data=x["Reservations"]

#automation code
    li=[]
        for instances in data:
            instance=instances["Instances"]
            for ids instance:
                instance_id=ids["InstanceId"]
                li.append(instance_id)
                print(instance_id)

#automation code final: 

ec2_client.terminate_instance(InstanceIds=li)
