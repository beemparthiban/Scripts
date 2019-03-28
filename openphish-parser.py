import json
import requests
import tldextract
from prettytable import PrettyTable
from collections import Counter
import os


# input  file
with open('phish.txt', 'r') as f:
    data = f.read()
    f.close()
    #print (data)

# splitting the result lines and removing any unwanted space since the output has multiple JSON lines instead of a single JSON blob.
result = data.strip().split('\n')

# using list comprehension converting each line to JSON
json_data = [json.loads(row) for row in result]

# using map function to call a particular JSON element and stripping out the '.' at end of the line.
urls = list(map(lambda d: d['url'], json_data))

# printing the URL's from the JSON
print ("The Phishing URL's are:")
for i in urls:
    print (i)

# using counter to count the items in the list and using the tldextract module to sp. It uses list comprehension.
c = Counter(tldextract.extract(tld).suffix for tld in urls)

# using counter to count the domains observed in the list. By using tldextract to extract domains from the URL's
dom = Counter(tldextract.extract(tld).registered_domain for tld in urls)

# creating a table to display the TLD output
tld_table = PrettyTable()
tld_table.field_names = ["TLD_name", "Count"]

print()
print ("Top level domain stats: \n ")
# adding values to the table and sorting the table using most_common() inbuilt function
for key, val in c.most_common():
    tld_table.add_row([key, val])
print(tld_table)

# creating a table to display the domain output
tld_table = PrettyTable()
tld_table.field_names = ["Domain_name", "Count"]

print()
print ("Unique phishing pages on Domain: \n ")
# adding values to the table and sorting the table using most_common() inbuilt function
for key, val in dom.most_common():
    tld_table.add_row([key, val])
print(tld_table)
