import json
import requests
import csv
import os
import pandas

f = open("api_key", "r")
api_key = f.read()
f.close()

f = open("username", "r")
username = f.read()
f.close()

if not os.path.exists("githubjsondata"):
	os.mkdir("githubjsondata")

githubsession = requests.Session()
githubsession.auth = (username, api_key)


access_point = "https://api.github.com"

file = csv.reader(open("midtermparsedfiles/noduplicatedataset.csv"), delimiter = ",")
names = list(file)

for i in range (0,640):
	user_url = names[i][0]
	result = json.loads(githubsession.get(access_point + "/users/" + user_url).text)
	f = open("githubjsondata/" + user_url + ".json", "w")
	f.write(json.dumps(result))
	f.close()
	