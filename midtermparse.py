from bs4 import BeautifulSoup
import pandas

import os
import glob

if not os.path.exists("midtermparsedfiles"):
	os.mkdir("midtermparsedfiles")


df = pandas.DataFrame()
for file_name in glob.glob("midtermhtmlfile/midterm.html"):
	#file_name = "midterm.html"
	f = open(file_name, "r")
	#file_content = f.read()

	soup = BeautifulSoup(f.read(), "html.parser")
	f.close()




	mydivs = soup.find_all("div",{"class":"userid"})
	for mydiv in mydivs:
		#mydiv = mydivs[0]
		githubid = mydiv["ghid"]
		df = df.append({
				'ID' : githubid
				}, ignore_index = True)

df.to_csv("midtermparsedfiles/midtermdataset.csv",index = False, header = False)
#print(mydivs)
