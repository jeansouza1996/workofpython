# from main import User
import unittest
import json
import requests

"""
rPut = requests.put("http://127.0.0.1:5000")
rDelete = requests.delete("http://127.0.0.1:5000/")
rPost = requests.post("http://127.0.0.1:5000/")
rGet = requests.get("http://127.0.0.1:5000/")
"""


class TesteNome(unittest.TestCase):

    def test_delete(self):
        response = requests.delete("http://127.0.0.1:5000/user/Jiraya")

        self.assertEqual(b'"Jiraya est\\u00e1 deletado."\n', response.content)

    def test_post(self):
        response = requests.post("http://127.0.0.1:5000/user/Jiraya?age=30&occupation=TI")
        u = json.loads(response.content)

        self.assertEqual("Jiraya", u['name'])
        self.assertEqual(30, int(u['age']))
        self.assertEqual("TI", u['occupation'])

    def test_put(self):
        response = requests.put("http://127.0.0.1:5000/user/Jiraya?age=35&occupation=RH")
        u = json.loads(response.content)

        self.assertEqual("Jiraya", u['name'])
        self.assertEqual(35, int(u['age']))
        self.assertEqual("RH", u['occupation'])


if __name__ == '__main__':
    unittest.main()
