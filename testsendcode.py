import requests, json
payload ={'temp' : 70}
headers = {'content-type': 'application/json'}
r = requests.post("http://remote-light.herokuapp.com/echo/", data=json.dumps(payload),headers = headers)
print r.text
