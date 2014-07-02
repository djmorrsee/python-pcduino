# Copyright (C) 2014 Daniel Morrissey & Andrey Shprengel
#
# Everyone is permitted to copy and distribute verbatim or modified
# copies of this license document, and changing it is allowed as long
# as the name is changed.

"""Wrapper function for sleep"""
import time

def delay(ms):
  """Freezes for ms milleseconds

  :param ms: milleseconds
  :type ms: int
  """
  time.sleep(ms / 1000.0)
