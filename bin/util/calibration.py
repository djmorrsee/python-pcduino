from bin.util.crono import *

# Averages out the value returned from function(args) deg times with ms delay
def SmoothReading(func, deg, *args):
  assert deg > 0

  val = 0
  for i in range(0, deg):
    val += func(*args)
    delay(100)
  return val / deg
