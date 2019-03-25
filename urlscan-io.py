import requests
from bs4 import BeautifulSoup
import json
import re

#the url_list is to store the extracted results.
url_list= []
api_address = 'https://urlscan.io/api/v1/search/?'
search_criteria = 'q='
limit_result = '&size=100'

#get input from user to search for domain or IP address
user_input = input("Enter domain or IP address: ")
#print(user_input)
pat = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
test = pat.match(user_input)
if test:
    ip_search = 'q=ip:'
    final_url = api_address+ip_search+user_input+limit_result
    #print(final_url)
else:
    domain_search = 'q=domain:'
    final_url = api_address+domain_search+user_input+limit_result
    #print(final_url)

json_data = requests.get(final_url).json()
total = json_data['total']

print("Number of times the domain/IP is scanned : " + str(total))


for item in json_data['results']:
    url_strip = item['page']['url']
    url_list.append(url_strip)
    print(url_strip)

#removing dupliates from the result. This will get it's input from the list url_list
uniq_urls = set(url_list)
print()
#printing the unique values
print("The unique URLs are: \n")
for url in uniq_urls:
    print(url)
