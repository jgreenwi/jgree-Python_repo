#Create DynamoDB table using boto
import boto3

# replace the keys below

dynamodb = boto3.resource(
    'dynamodb',
    aws_access_key_id='AKIAW2L4ZXZGPQ6UVGFF',
    aws_secret_access_key='YVHeDk9fkqNBbGglNkUEnruE+/EYG1Ci6i5pP4BD',
    )

dynamodb = boto3.client('dynamodb')

response = dynamodb.create_table(
    AttributeDefinitions=[
        {
            'AttributeName': 'ID',
            'AttributeType': 'S',
        }
    ],
    KeySchema=[
        {
            'AttributeName': 'ID',
            'KeyType': 'HASH',
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 1,
        'WriteCapacityUnits': 1,
    },
    TableName='DisneyAttractions',
)

print(response)