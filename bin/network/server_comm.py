## @package Server_comm
#functions fot formatting data and using the servers REST API
import requests, json

##GET
def GetDataFromServer(url):
	r = requests.get(url)
	return r

##POST
def PostJSONToServer(json_data, url):
	headers = {'content-type': 'application/json'}
	r = requests.post(url, data=json.dumps(json_data),headers=headers)
	return r

##DELETE
def DeleteJSONToServer(json_data, url):
	headers = {'content-type': 'application/json'}
	r = requests.delete(url, data=json.dumps(json_data),headers=headers)
	return r

## Used to format sensor data into JSON
def FormReadingJSON(m_id, m_auth_id, temp, light):
	data = {}
	data.update({'module_id':m_id})
	data.update({'module_auth_id':m_auth_id})
	reading = {'temperature':temp, 'light':light}
	data.update({'reading':reading})
	return data
	
## Used to form registration data into JSON
def FormRegistrationJSON(auth_id):
	data = { "auth_id" : auth_id }
	return data
