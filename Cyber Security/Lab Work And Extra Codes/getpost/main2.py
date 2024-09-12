#posting forms
# to post we need action url and names of inputs

import requests
from BeautifulSoup import BeautifulSoup

def request(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass
target_url = "http://192.168.254.129/mutillidae/index.php?page=dns-lookup.php"
response = request(target_url)

parsed_html = BeautifulSoup(response.content)
forms_list = parsed_html.findAll("form")
print(forms_list)


for form in forms_list:
    action = form.get("action")
    print(action) #get action url
    method = form.get("method")
    print(method) #get method url

    inputs_list = form.findAll("input")
    post_data = {} #make dictionary to post
    for input in inputs_list:
      input_name = input.get("name")
      input_type = input.get("type") #want to give input of type text only while entering value and post
      input_value = input.get("value") #default is value so dont change but if input is of type text then if condition..
      if input_type == "text":
          input_value = "test"    #enter value to exploit
      post_data[input_name] = input_value #input name is key and value is input value
        #before running on mutildaie write "test" and see what you are getting as result
        #you will get "result for test" same in output of program so it is vulnerable
    result = requests.post(target_url, data=post_data)
    print(result.content)
