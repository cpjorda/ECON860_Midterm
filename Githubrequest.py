import json
import requests

import os

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

rate_limit_url = access_point + "/rate_limit"
result = json.loads(githubsession.get(rate_limit_url).text)

print(result)
f.open("noduplicatedataset.csv", "r")
users = f.read()
f.close()

for user in users:
	user_url = access_point + "/users/" + user
	result = json.loads(githubsession.get(user_url).text)
	print(user)
	print(result['public_repos'])