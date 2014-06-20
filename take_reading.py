from bin.pcduino.adc import analog_read
from bin.network.server_comm import *
from bin.util.constants import *
from bin.util.calibration import *


import random
from bin.util.constants import *


import random


SERVER_URL = 'http://127.0.0.1:5000/module/post_reading/'
#SERVER_URL = 'http://remote-light.herokuapp.com/echo/'

#Use this for the duino
def GetReading(pin):
	return SmoothReading(analog_read, 10, pin)

#Use this on a non-arduino
def GetDummyReading(pin):
	return random.randint(0, 4096)

def Main():
	# Read Temp
	temp = SmoothReading(GetDummyReading, 10, 100, TEMP_PIN)
	#temp = GetReading(TEMP_PIN)

	# Read Light
	light = SmoothReading(GetDummyReading, 10, 100, LIGHT_PIN)
	#light = GetReading(LIGHT_PIN)

	# Send Data
	json_data = FormJSONData(MODULE_ID, MODULE_AUTH_ID, temp, light)
	PostJSONToServer(json_data, SERVER_URL)

	#PostData(SERVER_URL, temp, light, MODULE_ID)

Main()
