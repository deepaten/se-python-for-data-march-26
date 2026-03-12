import csv
# import particular methods from csv library
from csv import writer


fieldnames = ["Name", "age"]
data = [{"Name": "Deepa", "age": 25},
        {"Name":"Brad", "age":30},
        {"Name":"Joey", "age": 18}]

#open new file
with open("student_info.csv",mode="w",newline="") as csvfile:
    csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
    csvwriter.writeheader() # add header data
    csvwriter.writerows(data) # add data