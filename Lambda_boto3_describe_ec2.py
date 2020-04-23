import boto3 
from sys import argv

argKey = '$1'
argValue = '$2'

ec2client = boto3.client('ec2')
response = ec2client.describe_instances(Filters=[{'Name' : 'argKey','Values' : ['argValue']}])
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        # This sample print will output entire Dictionary object
        print(instance)
        # This will print will output the value of the Dictionary key 'InstanceId'
        print(instance["InstanceId"])