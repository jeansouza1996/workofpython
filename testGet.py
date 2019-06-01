import unittest
import json
import requests


def test_get(self):
    response = requests.get("http://127.0.0.1:5000/user/Jiraya")
    u = json.loads(response.content)

    self.assertEqual("Jiraya", u['name'])
    self.assertEqual(30, int(u['age']))
    self.assertEqual("TI", u['occupation'])