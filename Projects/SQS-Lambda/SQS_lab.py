import boto3

sqs = boto3.resource('sqs', region_name='us-east-1',
            aws_access_key_id="",
            aws_secret_access_key="")

queue = sqs.create_queue(QueueName='jgreeQueue')

print(queue.url)