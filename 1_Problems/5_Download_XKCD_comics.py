#! /library/Frameworks/Python.framework/Versions/3.5/python3.5
# ===================================================================================================
# In this program we will download all the XKCD comics

import os, bs4, requests

# Create the directory comics where we will store the images
if not os.path.isdir('./1_images'):
    os.mkdir('./1_images')

url_base = 'http://xkcd.com/'
url = url_base

# In this example we will download 10 latest pictures
for i in range(10):
    print('Downloading the URL: {}'.format(url))
    r = requests.get(url)
    r.raise_for_status()

    # creating soup object to search for image URL
    soup = bs4.BeautifulSoup(r.text, 'html.parser')

    # this select method will look for all div tags with id=comic then in those it will select img tags
    img_elements = soup.select('div[id="comic"] img')
    if len(img_elements) != 0:
        image_link = 'http:' + img_elements[0].get('src')
        file_name = os.path.basename(image_link)

        # getting the image using the requests module
        r1 = requests.get(image_link)

        # opening the file in our images directory with the name that equals basename
        file_object = open(os.path.join('1_images', file_name), 'wb')

        # writing image to a file
        print('\tCreating the file: {}'.format(file_name))
        for chunk in r1.iter_content(10000):
            file_object.write(chunk)
    else:
        print('\tCould not find any images at this URL')

    # now we will generate the next url to work with
    url_check = url
    url_elements = soup.select('a[rel="prev"]')
    if len(url_elements) != 0:
        url_next = url_elements[0].get('href')
        url_check = url_base + url_next[1:]

    if url == url_check:
        print('Can not get more URLs!')
        break
    else:
        url = url_check
print('Program finished downloading the items')
