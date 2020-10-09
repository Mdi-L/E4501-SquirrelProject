import csv

datareader = csv.reader(open('rows.csv'))

for i in datareader:
    print(i)
    break
