#used pip3 install to import the module
import requests
import json


#calling stack overflow api endpoint here
response = requests.get('http://api.stackexchange.com//2.3/questions?order=desc&sort=activity&site=stackoverflow')

#iterating and printing data that we have got from the endpoint

#prints response status code
print(response)

#prints the whole json reponse i.e. key(items) and value(list of questions)
#print(response.json())



#prints the value(list) and doesn't print the key(items)
print(response.json()['items'])



"""
for question in response.json()['items']:
    if question['answer_count'] == 0:
        print(question['title'])
        print(question['link'])
    else:
        print("answer count was not 0 so didn't print")
    print()
"""

