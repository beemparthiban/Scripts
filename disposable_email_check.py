import json
import requests
from prettytable import PrettyTable

url = 'https://open.kickbox.com/v1/disposable/'

# to store the final URL's to be queried against kickbox
api_urls = []


# creating a table to display the output
table = PrettyTable()
table.field_names = ["Email", "Result"]

# get the list of inputs from user and store it as a list
user_input = input("Enter the list of email addresses separated by commas: ")
input_list = user_input.split(',')
emails = [str(x.strip()) for x in input_list]

# form the URL's to be queried. place the user entered domains in a list at api_urls
for x in emails:
    final_url = url  + x
    api_urls.append(final_url)


# get the list of URL's from the list and query against the kickbox
for y in api_urls:
    json_data = requests.get(y).json()
    result = json_data['disposable']

# using another for loop to print the result and corresponding domain
for z in emails:
    table.add_row([z, result])   # adding result to the table
    #print(z,result)




print()
print ("Free email stats: \n ")

print(table)
