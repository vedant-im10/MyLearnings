# convert to full urls using urlparse
import ntpath

import requests
import re
import urllib.parse

from urllib3.util import url

target_url = "http://192.168.254.129/mutillidae/"


def extract_links_from(url):
    response = requests.get(url)
    return re.findall('(?:href=")(.*?)"', response.content)


href_links = extract_links_from(target_url)
for link in href_links:
    # link = target_url.join(link)
    u, err = url.parse(target_url)
    u.path = ntpath.join(u.path, link)
    s = u.string()
    print(s)
    print("------------------")
    # link = urlparse2.urljoin(target_url, link)  # join for conversion in full urls

# if target_url in link:  # i dont want to see third party links like fb...
#   print(link)
