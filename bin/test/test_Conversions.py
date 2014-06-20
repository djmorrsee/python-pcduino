
#!/usr/bin/env python2.7.7
# -*- coding: utf-8 -*-

# Andrey Shprengel
# Unittesting
import unittest
from bin.util.hardware_conversions import *


class ConversionTest(unittest.TestCase):

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
        
	def test_temp_conversion(self):
		reading = 100
		self.assertTrue( GetTemp(reading) in range (0,200))


# Main: Run Test Cases
if __name__ == '__main__':
	unittest.main()


