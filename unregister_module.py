# Copyright (C) 2014 Daniel Morrissey & Andrey Shprengel
#
# Everyone is permitted to copy and distribute verbatim or modified
# copies of this license document, and changing it is allowed as long
# as the name is changed.

from bin.network.server_comm import DeleteJSONToServer, FormRegistrationJSON
from bin.util.constants import MODULE_ID, AUTH_ID

SERVER_URL = 'http://remote-light.herokuapp.com/module/%i/' % MODULE_ID
# SERVER_URL = 'http://192.168.1.108:5000/module/%i/' % MODULE_ID

##Function for removoving  the pCduino from the server
def UnRegister():
	data = FormRegistrationJSON(AUTH_ID)
	r = DeleteJSONToServer(data, SERVER_URL)
	print(r.text)

UnRegister()
