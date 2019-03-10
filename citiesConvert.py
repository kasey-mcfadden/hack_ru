import json
import pandas
import sys
from random import randint

output = "var addressPoints = [\n"

with open('largest_cities.json') as f:
    data = json.load(f)

logStat = ["0 - Not Shipped", "1 - In Transit", "2 - Received"]

for x in data:
	lat = json.dumps(x["fields"]["coordinates"][0])
	lon = json.dumps(x["fields"]["coordinates"][1])
	output += ("[" + lat + ", " + lon + ", " + json.dumps(x["fields"]["city"]) + " Status: " + logStat[randint(0, 2)] + " Expiry: 2021-07-07T00:00:00.000Z" + "],\n")


output = output[:-2]
output += '\n];'

sys.stdout = open('OurData.js', 'w')
print(output)