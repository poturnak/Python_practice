#! /library/Frameworks/Python.framework/Versions/3.5/python3.5
# ===================================================================================================
# __________________ Requests module __________________
# requests.get('url') - function takes a string of a URL to download
#                     - you assign the response.get() to a variable
# requests.get('url', auth=('username', 'password')) - authentication using HTTPBasicAuth
# requests.post('url', data={'key': 'value') - make a post method request
# requests.get('url', params={'x': 'y'} - pass parameters as part of URL
# requests.get('url', headers={'header': 'value'} - create the list of headers
# __________________ Object parameters (object is 'r') __________________
# r.url - return used URL
# r.text - the html response is stored as a string (web page)
# r.json() - the json response stored as dictionary
# r.status_code - response status code (404, 200, etc.)
# r.headers['content-type'] - retrieve certain response headers
# print(r.headers) - print all response headers
# r.request.headers - access request headers
# r.encoding - retrieve encoding
# r.history - returns the list of redirects
# r.cookies - returns cookies
# raise_for_status(requests.objects) - this method will raise an exception if there was an error downloading the page
# __________________ Copy files and content to file __________________
# BINARY FILE - get the file using requests.get()
#             - open file using binary mode 'wb'
#             - loop over response.object.iter_content('chunk size')
#             - chunk size typically 100000 bytes (can be anyhting)
#             - call write to write on each iteration
#             - close the file
#             - see example below
# HTML - recommended to write in binary format as well
# # __________________ Working with POST requests and JSON __________________
# if you want to post data to site use
# requests.post('url', data={'':'', '':''} - in this case data will be form encoded
# if you want to pass data as a string use
# requests.post('url', data=json.dumps(dictionary) - passing data as a string
# ===================================================================================================

import requests, json, pprint

# getting the web page into the variable res
# also printing the web page contents
# res = requests.get('http://www.google.com/')

# by calling the method below we will raise the exception if there was an error downloading the page
# it is recommended that you use res.raise_for_status after the get request
# res.raise_for_status()

# we can also use try except for the raise_for_status()
# try:
#     res.raise_for_status()
# except Exception as err:
#     print("There was a problem with a download: {}".format(err))

# let's check the response status code
# print(res.status_code)

# let's copy the html back into the file
# html_file = open('html.html', 'w')
# html_file.write(res.text)
# html_file.close()

# let's copy binary file onto the disk
# res = requests.get('https://writeitdown31days.files.wordpress.com/2015/12/hello-picture.gif')
# res.raise_for_status()

# binary_file = open('binary.jpeg', 'wb')

# for chunk in res.iter_content(1000):
#     binary_file.write(chunk)
# binary_file.close()

# Let's prepare the list of parameters to send to the server
# payload = {'hello': 'world'}
# r = requests.get('http://www.facebook.com', params=payload)
# print(r.url)
# print(r.status_code)

r = requests.get('https://api.github.com/events')
for i, j in r.request.headers.items():
    print('{}: {}'.format(i,j))

str = json.loads(r.text)
pprint.pprint(r.json())

r = requests.get('http://www.facebook.com')
print(r.history)
for i, j in r.headers.items():
    print('{}: {}'.format(i,j))
print('\n\n')

print(r.cookies)
