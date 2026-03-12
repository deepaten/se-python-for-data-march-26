# Python script for extracting data from a CSV

import csv

#  extracts/import csv contents

rows = []
with open("employers.csv",newline="") as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)

print(f"The headers are: {header}")
print (rows)