import csv

# import particular methods from csv library
from csv import writer


header = ['Name', 'age']
data = [['Alex', 25], ['Brad', 30], ['Joey', 18]]

#open new file
with open("student_info.csv",mode="w",newline="") as csvfile:
    csvwriter = writer(csvfile)
    csvwriter.writerow(header) # add header data
    csvwriter.writerows(data) # add data




