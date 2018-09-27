#!/usr/bin/python

import boto3

def getipset(ipsetid):
    client = boto3.client('waf')
    response = client.get_ip_set (
        IPSetId=ipsetid, 
    )
    
    output = ""
    
    for key in response["IPSet"]["IPSetDescriptors"]:
       for value in key.iteritems():
          if value[1] != "IPV4":
             output += 'ip_set_descriptors {\n\ttype = "IPV4"\n\tvalue = "' + value[1] + '"\n}\n\n'
    
    return output

if __name__ == "__main__":
    ipsetid = raw_input("Enter IP Set ID: ")
    print(getipset(ipsetid))
