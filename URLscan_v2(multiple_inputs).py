import requests
import sys
import json


#the url_list is to store the extracted results.
url_list= []

#framing the URL
api_address = 'https://urlscan.io/api/v1/search/?'
search_criteria = 'q='
limit_result = '&size=100'
domain_search = 'q=domain:'


#get the list of inouts from user and store it as a list
api_urls = []
user_input = input("Enter the list of domains separated by commas: ")
input_list = user_input.split(',')
input_domains = [str(x.strip()) for x in input_list]


#form the URL's to be queried. place the user entered domains
for domain in input_domains:
    final_url = api_address+domain_search+domain+limit_result
    api_urls.append((final_url,domain)) #creating a tuple here.


#making the api call

for items in api_urls:
    json_data = requests.get(items[0]).json() #the items[0] specifies the final_url in the list from api_urls.
    try:
        if len(json_data["results"]) > 0:
            for item in json_data["results"]:
                url_strip = item[ 'result' ]
                url_list.append (url_strip)
                replaced = url_strip.replace("https://urlscan.io/api/v1/result/","https://urlscan.io/result/") #performing a replace for ease of vieweing.
                print(items[1],"-->",replaced)
        else:
            print (items[1] + ": URLSCAN doesn't have Intel on this domain! Try elsewhere!")

    except:
        print ("\n")
        print ("Error!")
        pass



