import boto3
#create queue

mysqs = boto3.client('sqs')

def create_queue(sqs, QueueName):
    response = sqs.create_queue(
        QueueName='jgree_que'
    )

print('Queue created')

