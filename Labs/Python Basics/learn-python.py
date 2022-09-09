some_string = "Hello Python"
print(some_string)
#this code creates a virtual environment 
python3 -m venv my_venv

#source my_venv/bin/activate



#boto3 is the name of the library we will use
#import boto3 -this is the first code 
#client vs resource: use client as a ref instead of resource. 
#s3 = boto3.client('s3')
#response = s3.list_buckets() ; this is calling a response
#what data type is response? dictionary
#buckets = response['Buckets'] ;this is showing where your response will be input
#for bucket in buckets:
    #print(bucket["Name"])
#upload object 
    #this file will upload itsself to the bucket 
    #import boto 3
    #make s3 variable
        #s3 = boto.client('s3')
        #response -->(go to the boto3 documentation for this part) [found in put_object]
        #response = s3.put_object(
        #body ='upload_object.py'---> template name
        #Bucket='example bucket name here'-> which bucket it should go to
        #keys="sample object file name")
        
    



