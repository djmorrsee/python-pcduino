from bin.pcduino.adc import analog_read
from bin.network.send_data import *
from bin.util.calibration import *

import random
from constants import *

SERVER_URL = 'http://127.0.0.1:5000/post_reading'

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
	PostData(SERVER_URL, temp, light, MODULE_ID)

Main()
