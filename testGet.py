import json
import unittest
import requests


class TesteNome(unittest.TestCase):
    def test_get(self):
        response = requests.get("http://127.0.0.1:5000/user/Jiraya")
        user_content = json.loads(response.content)
        self.assertEqual("Jiraya", user_content['name'])
        self.assertEqual(30, int(user_content['age']))
        self.assertEqual("TI", user_content['occupation'])


if __name__ == '__main__':
    unittest.main()
