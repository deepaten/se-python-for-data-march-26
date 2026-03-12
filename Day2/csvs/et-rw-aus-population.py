import csv

new_header = [{"Capital":"Melbourne"},
              {"Capital":'Sydney'},
               {"Capital":'Adelaide'},
                {"Capital":'Perth'},
                 {"Capital":'Hobart'},
                  {"Capital":'Brisbane'},
                   {"Capital":'Canberra'},
                    {"Capital":'Darwin'}]

rows = []
with open("australia-population.csv", newline="") as csvfile:
    csvreader = csv.DictReader(csvfile)
    i=0
    total_population=0
    for row in csvreader:
        row.update(new_header[i])
        total_population = total_population+ int(row["Population"])
        rows.append(row)
        i=i+1

print(rows)

fieldnames = ["State", "Population", "Capital"]
with open ("australia-population.csv", mode="w",newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print("Total Population of Australia is: ", total_population)
