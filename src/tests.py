import unittest
# src/tests.py
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import app as tested_app
import json

class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        tested_app.app.config['TESTING'] = True
        self.app = tested_app.app.test_client()

    def test_multiply_success(self):
        r = self.app.get('/multiply?a=5&b=2')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.data, b'10.0')
    
    def test_add_success(self):
        r = self.app.get('/add?a=5&b=2')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.data, b'7.0')
    
    def test_subtruct_success(self):
        r = self.app.get('/subtruct?a=5&b=2')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.data, b'3.0')
    
    def test_division_success(self):
        r = self.app.get('/division?a=5&b=2')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.data, b'2.5')

if __name__ == '__main__':
    unittest.main()