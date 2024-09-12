#look for sensitive file in directories
#these subdomains might contain no of directories which is not on main web site
#ip/directories...in a system
#this will help us to know which admin does not want us to know like login, password etc..
#show login,password, of mutillidae
import requests


def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass

target_url = "192.168.254.129/mutillidae/"

with open("/root/Downloads/files-and-dirs-wordlist.txt", "r") as wordlist_file: #to find posible directories on target web site
    #  content = wordlist_file.read() this will read whole file we want line by line
    for line in wordlist_file:
        word = line.strip() #removal of white space character
        test_url = target_url + "/" + word
        #print(test_url)
        response = request(test_url)
        if response:  #as try is there which will not float error, if is neccesary
            print("[+] discovered subdomain-->", test_url)
