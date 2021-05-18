import random
import json

res = []

for i in range(180001, 181200):
    dic = {'roll': str(i), 'coins': random.randint(400, 700)}
    res.append(dic)

for i in range(190001, 191200):
    dic = {'roll': str(i), 'coins': random.randint(400, 700)}
    res.append(dic)

for i in range(200001, 201200):
    dic = {'roll': str(i), 'coins': random.randint(400, 700)}
    res.append(dic)


infile = open("db.json", "a")
infile.write(json.dumps(res))

