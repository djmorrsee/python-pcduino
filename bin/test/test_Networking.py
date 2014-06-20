
#!/usr/bin/env python2.7.7
# -*- coding: utf-8 -*-

# Andrey Shprengel
# Unittesting
import unittest
from bin.network.send_data import *


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
        
	def test_normal_send(self):
		url = "http://remote-light.herokuapp.com/post_reading"
		light = 95
		temp = 84
		m_id = 2
		val = PostData(url, temp, light, m_id)
		self.assertEqual(val, 'Success')


# Main: Run Test Cases
if __name__ == '__main__':
    unittest.main()


