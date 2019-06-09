# from main import User
import unittest
import json
import requests


class TesteNome(unittest.TestCase):

    def test_delete(self):
        response = requests.delete("http://127.0.0.1:5000/user/Jiraya")

        self.assertEqual(b'"Jiraya est\\u00e1 deletado."\n', response.content)

    def test_post(self):
        response = requests.post("http://127.0.0.1:5000/user/Jiraya?age=30&occupation=TI")
        user_content = json.loads(response.content)

        self.assertEqual("Jiraya", user_content['name'])
        self.assertEqual(30, int(user_content['age']))
        self.assertEqual("TI", user_content['occupation'])

    def test_put(self):
        response = requests.put("http://127.0.0.1:5000/user/Jiraya?age=35&occupation=RH")
        user_content = json.loads(response.content)

        self.assertEqual("Jiraya", user_content['name'])
        self.assertEqual(35, int(user_content['age']))
        self.assertEqual("RH", user_content['occupation'])


if __name__ == '__main__':
    unittest.main()
