__author__ = 'sgr'

import os
import csv
import sys
import matplotlib.pyplot as plt

Wirkenergie = []
Wirkleistung_L1 = []
Wirkleistung_L2 = []
Wirkleistung_L3 = []
Wirkleistung = []

my_time = []
my_date = []

folder = 'D:\\34_Python\\Gesamt'

for filename in os.listdir(folder):

    #with open("D:\\04_Python\\Messzaehler\\UV2.1_P01_09.10.2015_12.07.03.csv", "r") as file:
    with open(folder + "\\" + filename, "r", encoding='utf16') as file:
        for i, line in enumerate(file):
            # Wirkenergie Wh
            if i == 8:
                splitted = line.split(";")
                Wirkenergie.append(splitted[2])
            # Wirkleistung Phase L1
            elif i == 17:
                splitted = line.split(";")
                Wirkleistung_L1.append(splitted[2])
            # Wirkleistung Phase L2
            elif i == 18:
                splitted = line.split(";")
                Wirkleistung_L2.append(splitted[2])
            # Wirkleistung Phase L3
            elif i == 19:
                splitted = line.split(";")
                Wirkleistung_L3.append(splitted[2])
            # Wirkleistung
            elif i == 20:
                splitted = line.split(";")
                Wirkleistung.append(splitted[2])


plt.plot(Wirkleistung)
plt.show()
