#this is a test code to make sure I can push to Github 
print("aws service project")
#sending another test message to git hub for lab 
#The following lines will begin our AWS Lab. Write Python Code below
#Create an empty list 
amazon_serv_list = [ ]
print(amazon_serv_list)
#Populate list with the insert or append command. Insert needs an argument of [2]. I'll demonstrate one value and then continue the rest with the append option. 
amazon_serv_list.insert(8, "CloudFormation")
print(amazon_serv_list)
amazon_serv_list.append("Cloud9"+ " "+"EC2"+ " "+"RDS"+ " "+ "ECS"+ " "+ "S3"+ " "+ "CodeBuild")
print(amazon_serv_list)
#let's add a timestamp to delay the next item on the list
import time
amazon_serv_list.append("DynamoDB")
print(amazon_serv_list)
time.sleep(2)
#This next command will delete an item on the list
del amazon_serv_list[2]
print(amazon_serv_list)
time.sleep(2)