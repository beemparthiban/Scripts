import json
import requests
import tldextract
from prettytable import PrettyTable
from collections import Counter

#setting up the URL variables
url = 'https://farsight-tlb01.threatstream.com/lookup/rrset/name/*.'
hdr = {
    'X-API-Key': 'xxxxx','Accept': 'application/json'
}
#getting user inout
domain = input("Enter the domain name: ")

#building the final url format
final_url = url+domain

#requesting the API
data = requests.get(final_url,headers=hdr)

#splitting the result lines since the output has multiple JSON lines instead of a single JSON blob.
result = data.text.strip().split('\n')


#using list comprehension converting each line to JSON
json_data = [json.loads(row) for row in result]


#using map function to call a particular JSON element and stripping out the '.' at end of the line.
rrnames = list(map(lambda d: d['rrname'].rstrip('.'), json_data))


#to print the unique resolutions of the domain in the past
rrdata = list(map(lambda e: e['rdata'], json_data))

#to print the unique resolutions of the domain in the past
rrtype = list(map(lambda f: f['rrtype'], json_data))

#unpacking the list of list to single list
#flat_list = [item for sublist in rrdata for item in sublist] --> not working as expected


# assign the unique values
unique_subdomains = sorted(list(set(rrnames)))


#table for printing the domains
domain_table = PrettyTable()
domain_table.field_names = ["Domain_Name","Record_Type", "IP/Name_Server"]


#reading from three lists to make it into a table
for dom, ip, type in zip(rrnames, rrdata, rrtype):
    if type == "A":  #extracting only the A records from the list
        parsed_ip = ''.join(ip) #converting list to string. Need to make it more efficient
        domain_table.add_row([dom,type,parsed_ip])

print(domain_table)

