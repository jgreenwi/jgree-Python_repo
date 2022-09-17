import json
import boto3
from datetime import datetime
client = boto3.client('sqs')

def lambda_handler(event, context):
        #Print Current Date and Time
    response = "The time and date is: "
    date_time = datetime.now()
    
    #Respond with sqs date and time
    message = client.send_message(
        QueueUrl='https://queue.amazonaws.com/468950040140/jgreeQueue',
        MessageBody=("This was sent on: " + str(date_time.strftime('%Y-%m-%d %H:%M:%S')))
        )
    return {
        'statusCode': 200,
        'body': json.dumps(message, indent=2)