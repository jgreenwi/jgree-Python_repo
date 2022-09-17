#Delete item from DynamoDB list with boto3
import boto3
Rank = 5
response = table.delete_item(
    Key={
        Primary_Column_Name: Rank
        }
    )
  
from