import json
import boto3
from datetime import datetime
client = boto3.client('sqs')

def lambda_handler(event, context):
        #Get the current date & time
    response = "The time and date is: "
    date_time = datetime.now()
    
    #send sqs message with the current date & time
    message = client.send_message(
        QueueUrl='https://queue.amazonaws.com/191325089225/week15-sqs-queue',
        MessageBody=("This was sent on: " + str(date_time.strftime('%Y-%m-%d %H:%M:%S')))
        )
    return {
        'statusCode': 200,
        'body': json.dumps(message, indent=2)