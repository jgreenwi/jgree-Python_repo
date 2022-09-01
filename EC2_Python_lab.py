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
