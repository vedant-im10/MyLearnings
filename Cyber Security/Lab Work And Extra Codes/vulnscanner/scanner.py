import requests
import re
import urlparse


class Scanner:
    def __init__(self, url):
        self.target_url = url
        self.target_links = []

    def extract_links_from(self, url):
        # if url == None:
        #     url =self.target_url
        response = requests.get(url)
        return re.findall('(?:href=")(.*?)"', response.content)

    def crawl(self, url=None):
        if url == None:
            url = self.target_url
        href_links = self.extract_links_from(url)
        # print(link)
        for link in href_links:
            # link = urlparse.urljoin(url, link)
            if 'http' or 'https' not in link:
                link = url.split('/')[0] + '//' + url.split('/')[2] + '/' + link
                print(link)

            if '#' in link:
                link = link.split('#')[0]

            if self.target_url in link and link not in self.target_links:
                self.target_links.append(link)
                print(link)
                self.crawl(link)  # call it self , recursive function
