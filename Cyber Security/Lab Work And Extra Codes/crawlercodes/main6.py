import requests
import re

target_url = "http://192.168.254.129/mutillidae/"

def extract_links_from(url):
    response = requests.get(url)
    return re.findall('(?:href=")(.*?)"', response.content)

href_links= extract_links_from(target_url)
for link in href_links:
    print(link)      #print linewise but some url will not be full urls so convert them in full urls

