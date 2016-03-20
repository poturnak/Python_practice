#! /library/Frameworks/Python.framework/Versions/3.5/python3.5
# ===================================================================================================
# +++++++++ Requests module +++++++++
# requests.get('url') - funciton takes a string of a URL to download
#                     - you assign the response.get() to a variable
# requests.object.text - the html response is stored as a string (web page)
# requests.object.status_code - response status code
# raise_for_status(requests.objects) - this method will raise an exception if there was an error downloading the page
# +++++++++ Copy files and content to file +++++++++
# BINARY FILE - get the file using requests.get()
#             - open file using binary mode 'wb'
#             - loop over response.object.iter_content('chunk size')
#             - chunk size typically 100000 bytes (can be anyhting)
#             - call write to write on each iteration
#             - close the file
#             - see example below
# HTML - recommended to write in binary format as well
# ===================================================================================================

import requests

# getting the web page into the variable res
# also printing the web page contents
res = requests.get('http://www.google.com/')

# by calling the method below we will raise the exception if there was an error downloading the page
# it is recommended that you use res.raise_for_status after the get request
res.raise_for_status()

# we can also use try except for the raise_for_status()
try:
    res.raise_for_status()
except Exception as err:
    print("There was a problem with a download: {}".format(err))

# let's check the response status code
print(res.status_code)

# let's copy the html back into the file
html_file = open('html.html', 'w')
html_file.write(res.text)
html_file.close()

# let's copy binary file onto the disk
res = requests.get('https://writeitdown31days.files.wordpress.com/2015/12/hello-picture.gif')
res.raise_for_status()

binary_file = open('binary.jpeg', 'wb')

for chunk in res.iter_content(1000):
    binary_file.write(chunk)
binary_file.close()

