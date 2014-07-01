""" Program to Reset The Main Database

Requires Proper Authorization, and the server to be responding
"""
from bin.network.server_comm import DeleteJSONToServer, FormRegistrationJSON
from bin.util.constants import AUTH_ID

SERVER_URL = 'http://192.168.1.108:5000/reset/'


def ResetTable():
	""" Sends a request to reset our database

	"""
	data = FormRegistrationJSON(AUTH_ID)

	response = DeleteJSONToServer(data, SERVER_URL)

	print(response.text)

if __name__ == '__main__':
	ResetTable()
