#!/usr/bin/env python2.7.7

# Unittesting
#Only run this test on the pcdouino
import unittest
from bin.pcduino.adc import *


class NetworkTest(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
    pass

  @classmethod
  def tearDownClass(cls):
    pass

  def setUp(self):
    pass

  def tearDown(self):
    pass

  def test_proper_range(self):
    self.assertTrue(analog_read(1) in range (0, 4096))

  def test_all_pins(self):
    for i in range (0,6):
      self.assertTrue(analog_read(i) in range(4096))

# Main: Run Test Cases
if __name__ == '__main__':
    unittest.main()
