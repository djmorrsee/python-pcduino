import requests, json
payload ={'temp' : 75}
headers = {'content-type': 'application/json'}
r = requests.post("http://127.0.0.1:5000/echo/", data=json.dumps(payload),headers = headers)
