

#!/usr/bin/env python2.7.7
# -*- coding: utf-8 -*-

# Andrey Shprengel
# Unittesting
import unittest
from bin.util.calibration import *
class SmoothReadingTest(unittest.TestCase):

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
        
    def test_return(self):
        def return5():
            return 5;
        degree = 3;
        result = SmoothReading(return5, degree)
        self.assertEqual(result, 5)
        
    def test_bad_paramas(self):
        degree = 0 
        def return5():
            return 5;
        self.assertRaises(AssertionError, SmoothReading, return5, degree)
        
    def test_no_params(self):
        self.assertRaises(TypeError, SmoothReading)

# Main: Run Test Cases
if __name__ == '__main__':
    unittest.main()

