## @package hardware_conversions
# Functions for convertion hardware reading to human understantable values

##Get temperature in farinheght
#@param reading The reading from the hardware register 
def GetTemp(reading):
	value = reading
	voltage = (value * VOLT) / 4096.0	
	tempC = (voltage - 0.5) * 100.0
	tempF = (tempC * 9.0 / 5.0) + 32.0
	return tempF

##Get light 
#@param reading The reading from the hardware register 
#@return light in percent brightness
def GetLight(reading):
	value = reading/4096.0
	return value 


