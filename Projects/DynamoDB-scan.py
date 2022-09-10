#use boto to scan dynamodb table
import boto3
from boto3.dynamodb.conditions import Key, Attr

response = client.scan(
    TableName='DisneyAttractions',
 )

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Theme Parks')
response = table.scan(
     TableName='DisneyAttractions',
    FrilterExpression=Attr('Sr').gte(0)
    )
 
response = table.query(
    KeyConditionExpression=Key('Theme Park').eq('Universal Studios')
    )
items = response['Items']
print(items)

response = table.scan(
    FilterExpression=Attr('Rank').lt(2)
    )
items = response['Items']
print(items)
from boto3.dynamodb.conditions import Key
response = table.quetry(
    KeyConditionExpression=Key('Sr').eq(0))
response["Items"]