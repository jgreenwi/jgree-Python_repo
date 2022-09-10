import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.client('dynamodb')

response = dynamodb.put_item(
    Item={
   'ID':{
          'S': 'hsv9krNOqy'  ,
        },
        'Theme Park': {
            'S': 'Universal Studios',
        },
        'Ride': {
            'S': 'Harry Potter',
        },
        'Rank': {
            'S': '1',
        },
    'ID':{
          'S': 'u2Kket8QKP'  ,
        },
        'Theme Park': {
            'S': 'Hollywood Studios',
        },
        'Ride': {
            'S': 'Tower of Terror',
        },
        'Rank': {
            'S': '2',
        },
    'ID':{
          'S': 'ouvGYwXPze'  ,
        },
        'Theme Park': {
            'S': 'Hollywood Studios',
        },
        'Ride': {
            'S': 'Galaxys Edge',
        },
        'Rank': {
            'S': '3',
        },
    'ID':{
          'S': 'FurxXXkfui'  ,
        },
        'Theme Park': {
            'S': 'Animal Kingdom',
        },
        'Ride': {
            'S': 'Flight of Passage',
        },
        'Rank': {
            'S': '4',
        },
    'ID':{
          'S': 'So1bPsGjst'  ,
        },
        'Theme Park': {
            'S': 'Universal Studios',
        },
        'Ride': {
            'S': 'Incredible Hulk',
        },
        'Rank': {
            'S': '5',
        },    
    
    },
    ReturnConsumedCapacity='TOTAL',
    TableName='DisneyAttractions',
)
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Theme Park')
response = table.scan(
     TableName='DisneyAttractions',
 #   FrilterExpression=Limit('Rank').gte(0)
      ExpressionAttributeValues={
        'Rank': {
            'N': '1'
 },
 ConsistentRead=True|False
 )
            
print(table.scan)