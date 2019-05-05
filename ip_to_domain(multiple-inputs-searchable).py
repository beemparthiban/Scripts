import json
import requests
import tldextract
from prettytable import PrettyTable


#setting up the URL variables
url = 'https://farsight-tlb01.threatstream.com/lookup/rdata/ip/'
hdr = {
    'X-API-Key': 'xxx','Accept': 'application/json'
}

#to store the final URL's to be queried against farsight api
api_urls = []

#to store the result set from the API
domains = []
ips = []
types = []

#get the search term from user
print("Just press enter if you don't want to search results!")
search_input = input("Enter the list of keywords to search in the resultset: ")

search_list = search_input.split(',')
search_words = [str(x.strip()) for x in search_list]

#get the list of inouts from user and store it as a list
user_input = input("Enter the list of IP's separated by commas: ")
input_list = user_input.split(',')
numbers = [str(x.strip()) for x in input_list]

#form the URL's to be queried. place the user entered domains
for item  in numbers:
    final_url = url + item
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


#creating a table
domain_table = PrettyTable()
domain_table.field_names = ["Domain_Name", "IP"]

#the below statements are to unpack the lists, so that we can print it. ( flatten list or list comprehension)
domains = [y for x in domains for y in x]
ips = [y for x in ips for y in x]


#this for loop prints all the result with A records. No user search is permitted.
# for dom, ip, type in zip(domains,ips):
#     domain_table.add_row([dom, ip])
# print(domain_table)

#this for loop is to get multiple user search input and print the result
for dom, ip in zip(domains,ips):
    for keys in search_words:
        if keys in dom:  #to apply the user search criteria
            domain_table.add_row([dom,ip])
print(domain_table)
