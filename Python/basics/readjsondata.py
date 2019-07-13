import json

data = []
with open('test.json') as f:
    for line in f:
        data.append(json.loads(line))