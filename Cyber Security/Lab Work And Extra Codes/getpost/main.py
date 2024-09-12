import requests
#parsing html code to python to get forms
#parse html codesing beautifulsooup library
from BeautifulSoup import BeautifulSoup
#here iis showing an error but will run
#here on dns lookup page of mutildaie ,we only have one for so it will display only one form for us
#but if it is having multiple forms beautifulsoup will retrieve all
#facebook registration form replacement to check vulnerability
#use text box to check vulnerability

def request(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass

target_url = "http://192.168.254.129/mutillidae/index.php?page=dns-lookup.php"
response = request(target_url)
#print(response.content) #to get the html code of url
#we can use regex to extract content of inspect element of post in text box
#but regex will be too complex so use beautifulsoup to et forms of html code
parsed_html = BeautifulSoup(response.content)
forms_list = parsed_html.findAll("form") #show form from inspect element, you can print element from page you want like a tag
#show two inputs from inspect element
print(forms_list) #print each element as a form from target html page

