import urllib.request
import os



f = open("api_key", "r")
api_key = f.read()
f.close()


if not os.path.exists("githubjsondata"):
	os.mkdir("githubjsondata")

urllib.request.urlopen()
