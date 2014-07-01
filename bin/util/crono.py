"""Wrapper function for sleep"""
import time

def delay(ms):
  """Freezes for ms milleseconds
  
  :param ms: milleseconds 
  :type ms: int
  """
  time.sleep(ms / 1000.0)
