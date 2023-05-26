#https://stackoverflow.com/questions/19123245/inserting-into-a-html-file-using-python
#https://stackoverflow.com/questions/16523939/how-to-write-and-save-html-file-in-python
#https://www.crummy.com/software/BeautifulSoup/bs4/doc/#bs4.Tag.name
#https://stackoverflow.com/questions/9028036/how-to-link-multiple-scripts
#https://docs.python.org/3/tutorial/modules.html

import requests
import filename
from bs4 import BeautifulSoup as Soup

page = requests.get("https://www.theatlantic.com/") # set the page url
soup = Soup(page.content, 'html.parser') # soup the page
headlines = soup.findAll('a', attrs={"class": "Latest_link__sXKHj"}) # get all the headlines

html_start = """
<!DOCTYPE html>
<html>
<head>
</head>
<body>
"""

#open("headlines.html", "w").close() #clear headlines file
filename_ = filename.main()
file = open(filename_, "w") #open headlines file
file.write(html_start) # write the starting html
# for loop will insert each a tag into the file
for headline in headlines:
    #delete all classes and things the Atlantic made
    del headline['data-event-element']
    del headline['data-action']
    del headline['class']
    del headline.h3['class']
    del headline.h3['data-event-element']
    headline_string = str(headline) + "\n" # turn the headline Tag into string
    file.write(headline_string) # put the headline into the string

html_end = "</body>"
file.write(html_end) # put the ending html into the file
file.close() # close the file