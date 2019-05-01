import json
import requests
import tldextract
from prettytable import PrettyTable


#setting up the URL variables
url = 'https://farsight-tlb01.threatstream.com/lookup/rrset/name/*.'
hdr = {
    'X-API-Key': 'xxxx','Accept': 'application/json'
}

#to store the final URL's to be queried against farsight api
api_urls = []

#to store the result set from the API
domains = []
ips = []
types = []

#get the search term from user
search_input = input("Enter the keyword to search in the resultset: ")


#get the list of inouts from user and store it as a list
user_input = input("Enter the list of domains separated by commas: ")
input_list = user_input.split(',')
numbers = [str(x.strip()) for x in input_list]

#form the URL's to be queried. place the user entered domains
for domain in numbers:
    final_url = url + domain
    api_urls.append(final_url)

#requesting the API
for words in api_urls:

    data = requests.get(words,headers=hdr)
    result = data.text.strip().split('\n') #splitting the result lines since the output has multiple JSON lines instead of a single JSON blob.
    json_data = [json.loads(row) for row in result] #using list comprehension converting each line to JSON
    rrname = list(map(lambda d: d['rrname'].rstrip('.'), json_data))
    domains.append(rrname)
    rrdata = list(map(lambda e: e['rdata'], json_data))
    ips.append(rrdata)
    rrtype = list(map(lambda f: f['rrtype'], json_data))
    types.append(rrtype)

#creating a table
domain_table = PrettyTable()
domain_table.field_names = ["Domain_Name","Record_Type", "IP"]

#the below statements are to unpack the lists, so that we can print it. ( flatten list or list comprehension)

domains = [y for x in domains for y in x]
ips = [y for x in ips for y in x]
types = [y for x in types for y in x]

#this for loop filters the user entered keyword in the result set and prints it
for dom, ip, type in zip(domains,ips,types):
    if search_input in dom:  #to apply the user search criteria
        if type == "A":     #to filter only A records
            domain_table.add_row([dom, type, ','.join(ip)])
print(domain_table)

#this for loop prints all the result with A records. No user search is permitted.
for dom, ip, type in zip(domains,ips,types):
    if type == "A":     #to filter only A records
        domain_table.add_row([dom, type, ','.join(ip)])
print(domain_table)
