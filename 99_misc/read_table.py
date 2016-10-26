import pandas as pd
from pandas import DataFrame


import csv
csvfile = open('table.csv')
spamreader = csv.reader(csvfile)

data = []

for row in spamreader:
    data.append(row)

data2 = []
for row in data:
    if row[1] == '7':
        data2.append(row)

data3 = []
for row in data2:
    found = False
    for ele in row:
        if ele == '\\N':
            found = True

    if found == False:
        data3.append(row)


with open('Table_Hauptanschluss.csv', "wb") as ofile:
    writer = csv.writer(ofile, delimiter=',')
    for row in data3:
        writer.writerow(row)


