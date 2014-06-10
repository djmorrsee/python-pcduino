from bin.util.crono import *

# Averages out the value returned from function(args) deg times with ms delay
def SmoothReading(func, deg, ms=100, *args):
  val = 0
  for i in range(0, deg):
    val += func(*args)
    delay(ms)
  return val / deg
