#extracting forms , so from given url i can extract all forms from extract_forms
import requests
import re
import urlparse
from BeautifulSoup import BeautifulSoup

class Scanner:
    def __init__(self, url, ignore_links):
        self.session = requests.Session() #creating session object which will create our current session
        #once log in is performed it will be stored in self.session
        self.target_url = url
        self.target_links = []
        self.links_to_ignore = ignore_links

    def extract_links_from(self, url):
        response = self.session.get(url) #all get post with session now
        return re.findall('(?:href=")(.*?)"', response.content)

    def crawl(self, url=None):
       if url == None:
          url =self.target_url
          href_links = self.extract_links_from(url)
          for link in href_links:
            #link = urlparse.urljoin(url, link)
            if 'http' or 'https' not in link:
                link = url.split('/')[0] + '//' + url.split('/')[2] + '/' + link
                print(link)

            if '#' in link:
                link = link.split('#')[0]
                print(link)
                    # in some links there are two elements first is before # and second is after that
                    # we are interested before # so we will take that and bypass second

            if self.target_url in link and link not in self.target_links and link not in self.links_to_ignore:
                # first not is for duplicacy of links
                self.target_links.append(link)
                print(link)
                self.crawl(link)

    def extract_forms(self, url):
        response = self.session.get(url) #get request through session
        parsed_html = BeautifulSoup(response.content)
      #  print((parsed_html.findAll("form")))
        return parsed_html.findAll("form")

    def submit_form(self, form, value, url):
        action = form.get("action")
        #print(action)  # get action url
        method = form.get("method")
        #print(method)  # get method url

        inputs_list = form.findAll("input")
        post_data = {}
        for input in inputs_list:
            input_name = input.get("name")
            input_type = input.get("type")
            input_value = input.get("value")
            if input_type == "text":
                input_value = value  #the same value that we used for submit form method
            post_data[input_name] = input_value  #post request
        if method == "post":
            return self.session.post(url, data=post_data)
        #print(url)
        #print((post_data))
        print(url + "?name=" + post_data["name"])
        return self.session.get(url + "?name=" + post_data["name"])
        #return self.session.get(url, data=post_data)#for xss reflected
    # all methods are not post some are get also like xss reflected inspect element is having get method
    #go in dvwa --> xss reflected--> inspect element in text box

    def run_scanner(self):
        for link in self.target_links:
            forms = self.extract_forms(link) #extract all forms from given link one by one which are discovered
            for form in forms:
                print("[+] testing form in" + link)
                    #here we can write vulnerability methods to discover vulnerability in forms

            if "=" in link:
                print("[+] testing " + link)
                    # here also we can write vulnerability methods to discover vulnerability in link


        #here we are discovering vulnerability in forms not in links
    def test_xss_in_form(self, form, url): #security level to medium in dvwa from terminal of metasploit
            #url of page which contains this forms that we have to give
            # in dvwapage.inc.php make security = medium
        xss_test_script = "<sCript>alert('test')</scriPt>" #change way of writing script in medium security to bypass filtering
        response = self.submit_form(form, xss_test_script, url)
        #print(response.content)
        if xss_test_script in response.content:
            return True  #means in inspect element check you will be having script executed , page is vulnerable

            #try out actually in xss reflected in dvwa
