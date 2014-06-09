from bin.pcduino.adc import analog_read
from bin.network.send_data import *
from bin.util.calibration import *
import random

# Our boards voltage
VOLT = 3.3

# 0,1 are 6 bit; 2-4 are 12 bit
TEMP_PIN = 4
LIGHT_PIN = 2

THIS_MODULE_NUMBER = 1 # Set yours to 2 if you notice!!!

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
	PostData(SERVER_URL, temp, light, THIS_MODULE_NUMBER)

Main()
