#!/usr/bin/env python
"""

This file is the main function that the pcduino will run.
It will take a reading from the sensors and the send the data to the server.
It will also send an API requests to delete all data older than 24 hours.
"""

from bin.pcduino.adc import analog_read
from bin.network.server_comm import *
from bin.util.constants import *
from bin.util.calibration import *
from bin.util.authorization import *

from drop_old import DropOld
import random

#SERVER_URL = 'http://127.0.0.1:5000/module/post_reading/'
#SERVER_URL = 'http://remote-light.herokuapp.com/module/post_reading/'
SERVER_URL = 'http://192.168.1.108:5000/module/post_reading/'

def GetReading(pin):
	""" Function for getting an averaged reading from one of the sensor pins.

	:param pin: the pin number the sensor requested
	:type pin: int
	:returns: double -- the averaged reading from the pin

	"""

	return SmoothReading(analog_read, 10, pin)


def GetDummyReading(pin):
	""" A funnction for get a fake reading for testing

	:returns: self explanatory
	"""
	return random.randint(0, 4096)

def TakeReading():
	""" Take Sensor Readings

	This function will take light and temperature raadings, format the data
	into JSON and send it our server. It will print the status code returned
	and will request that old data be deleted from the database
	"""
	#temp_pin_reading = SmoothReading(GetDummyReading, 10, TEMP_PIN)
	temp_pin_reading = GetReading(TEMP_PIN)



	#light_pin_reading = SmoothReading(GetDummyReading, 10, LIGHT_PIN)
	light_pin_reading = GetReading(LIGHT_PIN)


	m_auth_id = GetModuleAuthorizationID()
	json_data = FormReadingJSON(MODULE_ID, m_auth_id, temp_pin_reading, light_pin_reading)
	r = PostJSONToServer(json_data, SERVER_URL)
	print(r.text)

	DropOld()

if __name__ == '__main__':
	TakeReading()
