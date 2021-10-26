import urllib.request
import os
if not os.path.exists("midtermhtmlfile"):
	os.mkdir("midtermhtmlfile")

f = open("midtermhtmlfile/midterm.html","wb")

response = urllib.request.urlopen("http://45.79.253.243/index.html")
html = response.read()

f.write(html)
f.close()


