import csv
import collections
import math

d = {}
line_count = 0
with open('dino1.csv', 'r') as dino1:
    reader = csv.DictReader(dino1, delimiter=",")
    for row in reader:
        d[row['NAME']]  = row['LEG_LENGTH']
    print(d)
    