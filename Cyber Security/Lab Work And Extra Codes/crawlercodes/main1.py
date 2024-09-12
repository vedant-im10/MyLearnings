# try out different subdomain of website using wordlist
#mail.google.com

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
        test_url = line + target_url #each subdomain is ended with new line character so mail.google.com;
        print(test_url)
