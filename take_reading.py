from bin.pcduino.adc import analog_read
from bin.network.server_comm import *
from bin.util.constants import *
from bin.util.calibration import *
from bin.util.authorization import *
import random

SERVER_URL = 'http://192.168.1.108:5000/module/post_reading/'
#SERVER_URL = 'http://remote-light.herokuapp.com/echo/'

#Use this for the duino
def GetReading(pin):
	return SmoothReading(analog_read, 10, pin)

#Use this on a non-arduino
def GetDummyReading(pin):
	return random.randint(0, 4096)

def Main():
	# Read Temp
	# temp_pin_reading = SmoothReading(GetDummyReading, 10, 100, TEMP_PIN)
	temp_pin_reading = GetReading(TEMP_PIN)


	# Read Light
	# light_pin_reading = SmoothReading(GetDummyReading, 10, 100, LIGHT_PIN)
	light_pin_reading = GetReading(LIGHT_PIN)

	# Send Data
	m_auth_id = GetModuleAuthorizationID()
	json_data = FormReadingJSON(MODULE_ID, m_auth_id, temp_pin_reading, light_pin_reading)
	r = PostJSONToServer(json_data, SERVER_URL)
	print(r.status_code)
	print(r.text)

Main()
