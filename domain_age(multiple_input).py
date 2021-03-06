import requests
from bs4 import BeautifulSoup
import urllib.request
import time
start = time.time()

api_key = 'your_api_key'


url_1 = 'https://www.whoisxmlapi.com/whoisserver/WhoisService'

#to store the final URL's to be queried against whoisxml
api_urls = []

#get the list of inouts from user and store it as a list
user_input = input("Enter the list of domains separated by commas: ")
input_list = user_input.split(',')
numbers = [str(x.strip()) for x in input_list]

#form the URL's to be queried. place the user entered domains
for domain in numbers:
    final_url = url_1  + '?domainName=' + domain + '&apiKey=' + api_key + '&outputFormat=JSON'
    api_urls.append(final_url)

#get the list of URL's from the list and query against the WHOISXML
for words in api_urls:
    json_data = requests.get(words).json()
    domain = json_data['WhoisRecord']['domainName']
    age = json_data['WhoisRecord']['estimatedDomainAge']
    print(domain,age)


end = time.time()
print("Total time taken to execute the script: ", end - start,"secs")
