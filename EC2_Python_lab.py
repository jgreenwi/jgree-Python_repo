#EC2 + Boto + Python : you can use Boto3 to create/configure/and manage AWS services
#You are tasked with creating a list using Python that curates unique EC2 names that users can attach to instances. Python scripts should [allow users to input how many EC2 instances they want names for and output the same amount of names.] 
#Also, [allow users to input the name of their department that is used with the unique name]
#Then, [Generate random characters that will be included in the unique name]

#import boto3
#s3 = boto3.resource('s3')
import random
import string
from time import sleep

#create list of EC2 unique names
aws_dept = []
aws_dept = ["accounting", "marketing", "finops"]
ec2_name= int(len(input("Insert the amount of EC2 instances preferred")))

sleep(3)
letters= (string.ascii_letters+string.digits)
unique = ''.join(random.sample(letters,5))
#print(unique)
#below function gives you an unique EC2 name with a random generated departmet
result = (aws_dept)
aws_ec2_name= (unique)
print(random.choice(aws_dept), unique)
