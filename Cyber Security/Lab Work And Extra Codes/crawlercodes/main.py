
import requests

url = "hhghghghbh.google.com"
#url = "mail.google.com" #subdomain testing

get_response = requests.get("http://" + url)  #get request
print(get_response) #print http response code to test


# url= "dafsdfsdfmail.google.com" #sending garbage to check exception raised
#try:
#     get_response = requests.get("http://" + url)
 #     print(get_response)
 #except requests.exceptions.ConnectionError:
 #    pass