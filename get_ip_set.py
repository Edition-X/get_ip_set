#!/usr/bin/python

import boto3

ipsetid = raw_input("Enter IP Set ID: ")
client = boto3.client('waf')
response = client.get_ip_set (
    IPSetId=ipsetid, 
)

file = ""

for key in response["IPSet"]["IPSetDescriptors"]:
   for value in key.iteritems():
      if value[1] != "IPV4":
         file += 'ip_set_descriptors {\n\ttype = "IPV4"\n\tvalue = "' + value[1] + '"\n}\n\n'

print(file)
