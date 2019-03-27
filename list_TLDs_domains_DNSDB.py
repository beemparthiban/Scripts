import json
import requests
import tldextract
from prettytable import PrettyTable
from collections import Counter

#setting up the URL variables
url = 'https://farsight-tlb01.threatstream.com/lookup/rdata/ip/'
hdr = {
    'X-API-Key': 'your_api_key','Accept': 'application/json'
}
#getting user inout
ip = input("Enter the IP adress: ")

#building the final url format
final_url = url+ip

#requesting the API
data = requests.get(final_url,headers=hdr)

#splitting the result lines since the output has multiple JSON lines instead of a single JSON blob.
result = data.text.strip().split('\n')

#using list comprehension converting each line to JSON
json_data = [json.loads(row) for row in result]

#using map function to call a particular JSON element and stripping out the '.' at end of the line.
rrnames = list(map(lambda d: d['rrname'].rstrip('.'), json_data))

#print the output
#print (rrnames)

#using counter to count the items in the list and using the tldextract module to sp
c = Counter(tldextract.extract(tld).suffix for tld in rrnames)


#for keys,values in c.items():
    #print(keys)
    #print(values)

#creating a table to display the output
tld_table = PrettyTable()
tld_table.field_names = ["TLD_name", "Count"]

#adding values to the table and sorting the table using most_common() inbuilt function
for key, val in c.most_common():
   tld_table.add_row([key, val])
print (tld_table)

#table for printing the domains
domain_table = PrettyTable()
domain_table.field_names = ["Domain_Name"]

for dom in rrnames:
    domain_table.add_row([dom])
print(domain_table)
