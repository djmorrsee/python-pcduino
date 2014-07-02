# Copyright (C) 2014 Daniel Morrissey & Andrey Shprengel
#
# Everyone is permitted to copy and distribute verbatim or modified
# copies of this license document, and changing it is allowed as long
# as the name is changed.

""" Program to Reset The Main Database

Requires Proper Authorization, and the server to be responding
"""

from bin.network.server_comm import DeleteJSONToServer, FormRegistrationJSON
from bin.util.constants import AUTH_ID

SERVER_URL = 'http://remote-light.herokuapp.com/reset/'
# SERVER_URL = 'http://192.168.1.108:5000/reset/'


def ResetTable():
	""" Sends a request to reset our database

	"""
	data = FormRegistrationJSON(AUTH_ID)

	response = DeleteJSONToServer(data, SERVER_URL)

	print(response.text)

if __name__ == '__main__':
	ResetTable()
