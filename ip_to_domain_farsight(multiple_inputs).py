import json
import requests
import tldextract
from prettytable import PrettyTable
from collections import Counter

#setting up the URL variables
url = 'https://farsight-tlb01.threatstream.com/lookup/rdata/ip/'
hdr = {
    'X-API-Key': 'xxxxx','Accept': 'application/json'
}

#to store the final URL's to be queried against farsight api
api_urls = []

#get the list of inouts from user and store it as a list
user_input = input("Enter the list of IP's separated by commas: ")
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
    #rrtype = list(map(lambda f: f['rrtype'], json_data))
    #
    domain_table = PrettyTable()
    domain_table.field_names = ["Domain_Name", "IP"]

    #use this if you don't want the table, just the simple IP's
    # for dom, ip in zip(rrnames, rrdata):
    #     print(dom,ip)
    #
    #reading from three lists to make it into a table
    for dom, ip in zip(rrnames, rrdata):
        domain_table.add_row([dom,ip])

    print(domain_table)

