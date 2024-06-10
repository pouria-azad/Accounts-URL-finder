import requests
import random
import string
import pymongo

myClient = pymongo.MongoClient("mongodb://localhost:27017/")

myDB = myClient['SnapFood']
myCol = myDB['urls']

base_url = "https://pt.clickro.ir/view/"

def generate_random_string(length):
    characters = string.ascii_lowercase + string.digits
    return ''.join(random.choices(characters, k=length))

def send_request():
    random_string = generate_random_string(8)
    if not(myCol.find_one({'string':random_string })):
        url = base_url + random_string
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'}
        print(f"Trying URL: {url}")
        response = requests.get(url, headers= headers)
        if response.status_code != 200:
            myDict = {'string': random_string}
            myCol.insert_one(myDict)
            return send_request()
        else:
            print(random_string)
            return response.status_code
    else:
        send_request()   

# Test the function
counter = 0

print(send_request())