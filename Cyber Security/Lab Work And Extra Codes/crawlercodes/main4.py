#directly fetching link from html page of website from view page source
#first fetch html code of any web site


import requests


def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass

target_url = "192.168.254.129/mutillidae/"

response = request(target_url)
print(response.content) #this will print html code directly