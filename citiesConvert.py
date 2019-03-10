import json
import pandas
import sys
from random import randint

output = "var addressPoints = [\n"

with open('largest_cities.json') as f:
    data = json.load(f)

packStat = ["0 - Unpacked", "1 - Packed"]
logStat = ["0 - Not Shipped", "1 - In Transit", "2 - Received"]
table = []

for x in data:
	lat = json.dumps(x["fields"]["coordinates"][0])
	lon = json.dumps(x["fields"]["coordinates"][1])
	stat = logStat[randint(0, 2)]
	pack = packStat[randint(0, 1)]
	output += ("[" + lat + ", " + lon + ", " + "\"" + x["fields"]["city"] + " | Status: " + stat + " | Expiry: 2021-07-07T00:00:00.000Z" + "\"],\n")
	table.append([x["fields"]["city"], lat, lon, x["recordid"], pack, stat])
	

output = output[:-2]
output += '\n];'

df = pandas.DataFrame(table, columns=["city", "latitude", "longitude", "globalLocationNumber", "packStatus", "logisticStatus"])
df.to_html("generatedTable.html", classes="table")


sys.stdout = open('OurData.js', 'w')
print(output)