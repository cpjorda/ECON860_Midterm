import csv
rows = csv.reader(open("midtermparsedfiles/midtermdataset.csv", "r"))
newrows = []
for row in rows:
    if row not in newrows:
        newrows.append(row)
writer = csv.writer(open("midtermparsedfiles/noduplicatedataset.csv", "w"))
writer.writerows(newrows)