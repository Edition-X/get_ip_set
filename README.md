# get_ip_set
Python script to get IP's from WAF IP set and convert to Terraform

This script will output to stdout the IP CIDR ranges for the IP into a Terraform object for 'ip_set_descriptors'.
You can then redirect the stdout output into a seperate file.

`./get_ip_set.py > ips.tf`
