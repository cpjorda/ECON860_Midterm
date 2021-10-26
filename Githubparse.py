import json
import pandas
import os
import glob

if not os.path.exists("githubuserdata"):
	os.mkdir("githubuserdata")

df = pandas.DataFrame()

for file_name in glob.glob("githubjsondata/*.json"):
	f = open(file_name, "r")
	userdata = json.load(f)
	f.close()

	df = df.append({
			'ID': userdata['id'],
			'Avatar URL': userdata['avatar_url'],
			'URL': userdata['html_url'],
			'Number of Followers': userdata['followers'],
			'Number of Following': userdata['following'],
			'Number of Repos':userdata['public_repos'],
			'Name': userdata['name'],
			'Company': userdata['company'],
			'Blog' : userdata['blog'],
			'Location': userdata['location'],
			'Email': userdata['email'],
			'Hireable': userdata['hireable'],
			'Bio': userdata['bio'],
			'Starting Time': userdata['created_at'],
			'Last Update Time': userdata['updated_at'],
			'Twitter Username': userdata['twitter_username'],
			'Gists': userdata['public_gists']
			}, ignore_index = True)

df.to_csv("githubuserdata/gituserinformation.csv")