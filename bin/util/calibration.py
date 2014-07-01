""" This file is used for averaging return values
""" 
from bin.util.crono import *

def SmoothReading(func, deg, *args):
  """Avereges the return of func over deg times
  
  :param func: The function to be averaged
  :type func: function
  
  :param deg: how many times the function will be averaged
  :type deg: int 
  
  :param ms: time between function calls 
  :type ms: int 
  
  :param *args: the arguments to be passed to func
  """
  assert deg > 0

  val = 0
  for i in range(0, deg):
    val += func(*args)
    delay(100)
  return val / deg
