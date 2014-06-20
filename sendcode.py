import requests, json
import hardware_functions
current_temp = hardware_functions.readTemp()
payload ={'temp' : current_temp}
headers = {'content-type': 'application/json'}
r = requests.post("http://remote-light.herokuapp.com/echo/", data=json.dumps(payload),headers = headers)
print r.text
