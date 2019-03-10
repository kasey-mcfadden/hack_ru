import requests
import json

sn = ["180914578754", "180914579188", "180914580225", "180914581798", "180914582625", "180914582994", "180914584964", "180914585404", "180914586384", "180914587672", "180914588946", "180914589592", "180914590923", "180914591534", "180914592618", "180914593035", "180914594437", "180914595385", "180914596567", "180914597083", "180914598845", "180914599081", "180914600947", "180914601648", "180914602203", "180914603799", "180914604473", "180914605956", "180914606900", "180914607647", "180914607995", "180914609695", "180914610465", "180914611935", "180914613789", "180914614638", "180914615116", "180914616211", "180914617655", "180914618557", "180914619124", "180914620176", "180914621061", "180914622443", "180914624587", "180914628026", "180914629521", "180914630348", "180914631775", "180914632588", "180914633189", "180914634182", "180914635573", "180914636734", "180914637643", "180914638649", "180914639163", "180914640322", "180914641414", "180914642695", "180914643977", "180914644471", "180914645728", "180914646592", "180914647296", "180914648435", "180914649917", "180914650685", "180914651011", "180914652977", "180914653875", "180914654539", "180914655972", "180914656140", "180914657769", "180914658623", "180914659666", "180914660002", "180914661708", "180914662069", "180914663542", "180914664027", "180914665723", "180914666138", "180914667194", "180914668549", "180914669811", "180914670846", "180914671493", "180914672071", "180914673120", "180914674325", "180914675242", "180914676967", "180914677814", "180914678181", "180914679448", "180914680124", "180914681486", "180914683536", "180914684191", "180914685748", "180914686320", "180914687730", "180914688561", "180914689593", "180914690007", "180914691834", "180914692442", "180914693927", "180914694375", "180914695632", "180914696125", "180914697018", "180914698654", "180914699039", "180914700454", "180914701560", "180914702455", "180914703987", "180914704846", "180914705234", "180914706464", "180914707385", "180914708830", "180914709142", "180914710450", "180914711336", "180914712028", "180914713429", "180914714709", "180914715194", "180914716452", "180914717373", "180914718258", "180914719656", "180914720716", "180914721519", "180914722921", "180914723631", "180914724581", "180914727117", "180914728609", "180914729121", "180914730906", "180914731977", "180914732250", "180914733370", "180914734759", "180914735545", "180914736120", "180914737848", "180914738980", "180914739233", "180914740277", "180914741016", "180914742894", "180914743529", "180914744382", "180914745458", "180914746396", "180914747941", "180914748555", "180914749905", "180914750297", "180914751004", "180914752174", "180914753936", "180914754397", "180914755928", "180914756034", "180914757152", "180914758726", "180914759302", "180914760430", "180914761865", "180914762508", "180914763246", "180914764801", "180914765742", "180914766882", "180914767639", "180914768001", "180914769225", "180914770962", "180914771701", "180914772469", "180914773021", "180914774706", "180914775593", "180914776290", "180914777034", "180914778911", "180914779333", "180914780490", "180914781828", "180914782706", "180914783987", "180914784328", "180914785844"]
url = "https://mercklab-poc-sl-api.mybluemix.net/api/products/readbulk"
auth = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InRlc3RlckBtZXJjay5jb20iLCJpYXQiOjE1NTIxODM2MzAsImV4cCI6MTU1MjE5ODAzMH0.lsNIBhpWU6Z7Z_GolrP3pQc7YsdKkStm9YfGaid1GHw"
data = '{"product": ['

for x in sn:
	product = {
		"gtin": "08806555018611", 
		"serialNumber": x, 
		"lotNumber": "R036191", 
		"expiryDate": "2021-07-07T00:00:00.00Z"
	}
	data += json.dumps(product) + ", "

data = data[:-2]
data += ']}'
data = json.loads(data)

r = requests.post(url, json=data, headers={'Content-Type': 'application/json', 'Authorization': auth})

content = json.loads(r.content)
print(json.dumps(content, indent=4, sort_keys=True))
