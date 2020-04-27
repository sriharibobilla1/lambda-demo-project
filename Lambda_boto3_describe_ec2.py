import boto3 
from sys import argv

# Script will need 2 arg inputs while running

argKey = '$1'
argValue = '$2'

ec2client = boto3.client('ec2')

# This decsribes the EC2 Instances filtering with the tag:key/value

response = ec2client.describe_instances(Filters=[{'Name' : 'tag:argKey','Values' : ['argValue']}])
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        
        # Prints output entire Dictionary object
        
        print(instance)
        
        # Prints output the value of the Dictionary key 'InstanceId'
        
        print(instance["InstanceId"])
