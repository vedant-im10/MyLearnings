#websites having first page as login page so crawling will only result in one login link
# go to every possible page using crawler
#crawler code is used
import requests
import re
#import urlparse

class Scanner:
    def __init__(self, url, ignore_links): #scanner execution when instance of class scanner is created
        self.session = requests.Session() #creating session object which will create our current session
        #once log in is performed it will be stored in self.session
        self.target_url = url
        self.target_links = [] #make a list of possible link of my target website by crawling
        self.links_to_ignore = ignore_links

    def extract_links_from(self, url): #always in class first argument is self
        response = self.session.get(url) #all get post with session now
      #  print(response.content)
        return re.findall('(?:href=")(.*?)"', response.content)

    def crawl(self, url=None): #default value of argument of url
            #we can call url without specifying it so allow me to crawl without input arg
        if url == None: #method is called outside recursive call which is first page of target_url
            url =self.target_url
        href_links = self.extract_links_from(url)
            # change 1
        #link = href_links
        #print(link)
        for link in href_links:
                #link = urlparse.urljoin(url, link)
            if 'http' or 'https' not in link:
                link = url.split('/')[0] + '//' + url.split('/')[2] + '/' + link
                print(link)
            if '#' in link:
                link = link.split('#')[0]
                print(link)

            if self.target_url in link and link not in self.target_links and link not in self.links_to_ignore:
                self.target_links.append(link)
                print(link)
                self.crawl(link) #this is recursive function so each time it will call to completey different link
                    #if target_url is used then i will not be able to discover new links of web page
                    #it will only discover from target_url
