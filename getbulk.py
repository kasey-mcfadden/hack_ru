import requests
import json

url = "https://mercklab-poc-sl-api.mybluemix.net/api/products/readbulk"
auth = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InRlc3RlckBtZXJjay5jb20iLCJpYXQiOjE1NTIxODM2MzAsImV4cCI6MTU1MjE5ODAzMH0.lsNIBhpWU6Z7Z_GolrP3pQc7YsdKkStm9YfGaid1GHw"
data = '{"product": [{"gtin": "11234562345781", "serialNumber": "00000100000517190600", "lotNumber": "A98234", "expiryDate": "2019-06-01T04:00:00.000Z"}]}'
data = json.loads(data)

r = requests.post(url, json=data, headers={'Content-Type': 'application/json', 'Authorization': auth})

# print(json.dumps(data))
content = json.loads(r.content)
print(json.dumps(content, indent=4, sort_keys=True))
