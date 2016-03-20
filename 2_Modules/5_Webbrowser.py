#! /library/Frameworks/Python.framework/Versions/3.5/python3.5
# webbrowser.open(url, new=num) - has the nw parameter
#                          - 0 opens in the same browser window
#                          - 1 opens in new window
#                          - 2 opens in new tab
# webbrowser.open_new(url) - open in new window


import webbrowser
webbrowser.open_new('http://www.facebook.com')
print(webbrowser.get('firefox'))
