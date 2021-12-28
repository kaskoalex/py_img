
url = 'https://www.python.org/static/opengraph-icon-200x200.png'
 
# downloading with urllib
 
# imported the urllib library

 
 
# downloading with requests
 
# import the requests library
import requests
 
 
# download the url contents in binary format
r = requests.get(url)
 
# open method to open a file on your system and write the contents
with open("python1.png", "wb") as code:
    code.write(r.content)

