import requests
from bs4 import BeautifulSoup
import urllib.request


api_address = 'https://www.whoisxmlapi.com/whoisserver/WhoisService?apiKey='remove_quotes_and_put_your_api_key_here'&outputFormat=XML&domainName='
domain = input("enter the domain name: ")
#url_list= []
final_url = api_address+domain
print(final_url)
#source = requests.get(final_url)


source = urllib.request.urlopen(final_url).read()

soup = BeautifulSoup(source,'xml')


for data in soup:
    try:
        age = data.find('estimatedDomainAge').text
        email = data.find('contactEmail').text
        domain = data.find('domainName').text
        print("Domain Name: ", domain)
        print("Contact Email: ", email)
        print("Domain Age: ", age)
    except Exception:
        pass
