import csv
line_count = 0
d = {}

with open("../basics/dino1.csv", mode = 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        line_count += 1
        if not line_count:
            continue
        d[row['NAME']] = [row['LEG_LENGTH']]
        line_count = 0
    print(d)

with open("../basics/dino2.csv", mode = 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        line_count += 1
        if not line_count:
          continue
        if row['STANCE'] == 'bipedal':
            if row['NAME'] in d:
                d[row['NAME']].append(row['STRIDE_LENGTH'])

speed = {}
import math
for key, val in d.items():
    if len(val) == 2:
        speed[key] = ( float(val[1])/float(val[0]) - 1) * math.sqrt(float(val[0]) * 9.8)

print(sorted(speed.items(), key = lambda x: x[1], reverse = True))