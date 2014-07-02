# Copyright (C) 2014 Daniel Morrissey & Andrey Shprengel
#
# Everyone is permitted to copy and distribute verbatim or modified
# copies of this license document, and changing it is allowed as long
# as the name is changed.

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
