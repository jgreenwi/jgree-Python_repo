#EC2 + Boto + Python : you can use Boto3 to create/configure/and manage AWS services
#You are tasked with creating a list using Python that curates unique EC2 that users can attach to instances. Python scripts should [allow users to input how many EC2 instances they want names for and output the same amount of names.] 
#Also, [allow users to input the name of their department that is used with the unique name]
#Then, [Generate random characters that will be included in the unique name]

#import boto3
#s3 = boto3.resource('s3')
import random
import string
aws_ec2 = []

letters= string.ascii_letters
x ="".join(random.sample(letters,5))
print(x)

aws_ec2_name= (x)
print(x)

aws_ec2_name = input("What is your department name?")
print(input)

