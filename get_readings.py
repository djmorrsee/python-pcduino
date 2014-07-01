from bin.network.server_comm import *
from bin.util.constants import MODULE_ID
from pprint import pprint

# SERVER_URL = 'http://remote-light.herokuapp.com/module/%i/' % MODULE_ID
SERVER_URL = 'http://192.168.1.108:5000/module/%i/' % MODULE_ID

def GetReadings():
	data = GetDataFromServer(SERVER_URL)
	pprint(data.text)

GetReadings()
