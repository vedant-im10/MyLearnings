#after fetching html extract any useful data from that html over here
# inspect element will tell you for any imageobject tag refernace
#we are interested in tag referance
# <a tag and href to specify object link when user click
#use regex to do the stuff of extracting the same
#it will fetch all the links of any web page

import requests
import re


def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass

target_url = "192.168.254.129/mutillidae/"

response = request(target_url)
#href_links = re.findall('href=".*"', response) #accept any char which starts with href= upto next double quote
href_links = re.findall('(?:href=")(.*?)"', response.content) #use pythex to chk this functionality
#findall will find all substring which will match above format
# 1. non matching 2. non greedy group ->up to first double quote only
print(href_links) #this will print html code directly