import json
import requests
import tldextract
from prettytable import PrettyTable
from collections import Counter

#setting up the URL variables
url = 'https://farsight-tlb01.threatstream.com/lookup/rrset/name/*.'
hdr = {
    'X-API-Key': 'list_your_api_key','Accept': 'application/json'
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

# assign the unique values 
unique_subdomains = sorted(list(set(rrnames)))


#table for printing the domains
domain_table = PrettyTable()
domain_table.field_names = ["Domain_Name"]

for dom in unique_subdomains:
    domain_table.add_row([dom])
print(domain_table)
