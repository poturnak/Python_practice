#! /library/Frameworks/Python.framework/Versions/3.5/python3.5
# ===================================================================================================
# ______________________Working with soup object ______________________
# soup = bs4.BeautifulSoup('html', 'html.parser') - load html into beautiful soup
#                                                 - create an object you will work with
#                                                 - you also need to pass 'html.parser'
# print(soup.prettify()) = pretty print the soup object
# soup.title - returns title tags and title betwene the tags from the soup object
# soup.head, soup.a, etc.
# soup.title.string - returns title object (tags and string between tags)
# --you can also navigate into the child tags
# soup.body.a - get to body first, then within body tag get into a tag, will give you the fist object of tag <a>
# --to return all tags <a> use findall() method as below
# soup.findall('a') - returns all <a> tags as a list
# soup.find(id='id value') - returns tag with associated id
# soup.getTeXt() - return all the text from the soup
# ______________________Working with tags ______________________
# soup = bs4.BeautifulSoup('<b>Hello</b>', 'html.parser')
# tag = soup.b
# tag.name - gives name of tag
# tag['class'] - returns data associated with attribute class
# tag.attrs - returns dictionary of attributes
# --you can add, remove, and modify tags
# --you can access all children tags of a tag
# --they are returned as a list if you use contents attribute
# soup.head.contents - returns a list of tags within the <head>
# soup.head.parent - returns the parent tag
# ______________________Working with strings ______________________
# String is the text in between tags
# soup.b.string - returns the string between b tags
# tag.string - returns the string between the tags that were assigned to variable tag
# tag.string.replace_with('New string') - replace the string with the new one
# ______________________Searching the tree ______________________







# ______________________ Working with search results ______________________
# select() - returns a list of objects that were found
#          - it will be tags and contents within the tags
# soup[0].getText() - from the list get position 0 and return the information within the tag
# soup[0].attrs - return the attributes of the tag that was found
# soup[0].get('attribute name') - from the returned list, choose item, then apply get() method with attribute name
#                               - will return the value of the attribute

# ______________________Searching soup object 'soup' ______________________
# soup.select('div') - will choose all elements named <div>
# soup.select('#author') - the element with an id attribute author
# soup.select('.notice') - all elements that use css class named notice
# soup.select('div span') - All elements named <span> that are within an element named <div>
# soup.select('div > span') - All elements named <span> that are:
#                           - directly within an element named <div>
#                           - with no other element in between
# soup.select('input[name]') - All elements named <input> that have a name attribute with any value
# soup.select('input[type="button"]') - All elements named <input> that have an attribute named type with value button
# soup.select('p #author') - any element that has id author that is within p element
# ===================================================================================================

import requests, bs4
# r = requests.get('https://www.nostarch.com')
# r.raise_for_status()
# to_parse = bs4.BeautifulSoup(r.text, 'html.parser')

# opening local html file
file_object = open('example.html')
file_contents = file_object.read()

# creating soup object
soup = bs4.BeautifulSoup(file_contents, 'html.parser')
print(soup.title.string)
print(soup.body.contents)
print(soup.prettify())  # pretty printing
print('Separator'.center(50, '_'))

# searching the soup object for certain items
elements = soup.select('#author')

# now we will work with what we found
print(len(elements))
print(type(elements[0]))

print('\nHere is what we scraped:')
for element in elements:
    print(str(element), '\n')

print(elements[0].getText())  # get the text within the tag that we searched for
print(elements[0].attrs)  # get the dictionary ofd attributes for this tag

# if you have attributes, you can get them directly
# you choose the element of the list, then you apply get() method by passing the attribute name to it
print(elements[0].get('id'))
