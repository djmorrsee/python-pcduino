from bin.network.server_comm import *
from bin.util.authorization import *
from bin.util.constants import MODULE_ID, AUTH_ID

SERVER_URL = 'http://127.0.0.1:5000/module/%i/' % MODULE_ID

def Register ():
	data = FormRegistrationJSON(AUTH_ID)
	r = PostJSONToServer(data, SERVER_URL)
	if r.status_code == 200:
		if r.text != 'Bad Module ID':
			SaveModuleAuthorizationID(r.text)
			print('Registered')
		else:
			print (r.text)
	else:
		print('Not Registered')
		print(r.text)

def UnRegister():
	data = FormRegistrationJSON(AUTH_ID)
	r = DeleteJSONToServer(data, SERVER_URL)
	print(r.status_code)

Register()
