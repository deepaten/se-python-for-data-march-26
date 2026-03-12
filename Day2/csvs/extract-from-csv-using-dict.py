# Python script for extracting data from a CSV
import csv
#  extracts/import csv contents

rows = []
with open("employers.csv",newline="") as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        rows.append(row)


for line in rows:
    print(line)