import json
import requests
from prettytable import PrettyTable

url = 'https://open.kickbox.com/v1/disposable/'

# creating a table to display the output
table = PrettyTable()
table.field_names = ["Email", "Result"]

# get the list of inputs from user and store it as a list
user_input = input("Enter the list of email addresses separated by commas: ")
input_list = user_input.split(',')
emails = [str(x.strip()) for x in input_list]

# to store the final URL's to be queried against kickbox. using for loop to iterate through list of emails in the 'emails' list.
api_urls = [url + email for email in emails]

# get the list of URL's from the list and query against the kickbox
results = [requests.get(url).json().get('disposable') for url in api_urls]

# using zip to print the result and corresponding domain from two for loops
for email, result in zip(emails, results):
    table.add_row([email, result])   # adding result to the table
    #print(z,result)

print()
print ("Free email stats: \n ")
print("True -> It's a disposable email address")
print("False -> Not a disposable address")
print("\n")

print(table)
