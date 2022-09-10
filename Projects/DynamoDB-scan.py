#use boto to scan dynamodb table
import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb=boto3.resource("dynamodb")
table=dynamodb.Table('DisneyAttractions')

response=table.scan(
    FilterExpression=Attr('Rank').gte(2)
    )
print(response)
