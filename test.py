# coding: utf-8

import unittest
import requests

url = "http://localhost:8080"

class BitlyTest(unittest.TestCase):
    def test_redirect(self):
        full_url = "http://www.google.co.jp"
        short_url = requests.post(url, data=full_url, headers={"Content-Type":"text/plain"}).text
        r = requests.get(short_url)
        self.assertEqual(full_url, r.url)

if __name__=="__main__":
    unittest.main()
