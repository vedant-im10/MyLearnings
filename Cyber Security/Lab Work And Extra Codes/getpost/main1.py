#how to extract nested elements from the elements fetched in previous notebook
#form starts with <form and ends with </form same as script
#so we can write anything between start and end of the form
# action in inspect element and main url part is same , this may not be possible in other links
#everythin which start with < is actual html element
# action, method etc.. these are attributes of an element
#use findall for elements

# action is page where the form is submitted to when we enter in text box


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

    inputs_list = form.findAll("input") #input is actual html element not attribute

    for input in inputs_list:
        input_name = input.get("name")
        print(input_name)
