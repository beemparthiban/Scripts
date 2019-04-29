import json
import requests
import tldextract
from prettytable import PrettyTable
from collections import Counter

#setting up the URL variables
url = 'https://farsight-tlb01.threatstream.com/lookup/rrset/name/*.'
hdr = {
    'X-API-Key': 'xxxx','Accept': 'application/json'
}

#to store the final URL's to be queried against farsight api
api_urls = []

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
    rrnames = list(map(lambda d: d['rrname'].rstrip('.'), json_data))
    rrdata = list(map(lambda e: e['rdata'], json_data))
    rrtype = list(map(lambda f: f['rrtype'], json_data))

    domain_table = PrettyTable()
    domain_table.field_names = ["Domain_Name","Record_Type", "IP"]


#reading from three lists to make it into a table
    for dom, ip, type in zip(rrnames, rrdata, rrtype):
        if type == "A":  #extracting only the A records from the list
            parsed_ip = ','.join(ip) #converting list to string. Need to make it more efficient
            domain_table.add_row([dom,type,parsed_ip])

    print(domain_table)

