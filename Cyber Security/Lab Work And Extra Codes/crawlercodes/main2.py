#use of strip method to remove white space character

import requests


def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass

target_url = "google.com"

with open("/root/Downloads/subdomains-wodlist.txt", "r") as wordlist_file:
    #  content = wordlist_file.read() this will read whole file we want line by line
    for line in wordlist_file:
        word = line.strip() #removal of white space character
        test_url = word + "." + target_url
        #print(test_url)
        response = request(test_url)
        if response:  #as try is there which will not float error, if is neccesary 
            print("[+] discovered subdomain-->", test_url)
