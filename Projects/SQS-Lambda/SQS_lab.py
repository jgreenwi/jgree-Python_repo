import boto3

sqs = boto3.resource('sqs', region_name='us-east-1',
            aws_access_key_id="AKIAW2L4ZXZGBZWHCROQ",
            aws_secret_access_key="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")

queue = sqs.create_queue(QueueName='jgreeQueue')

print(queue.url)