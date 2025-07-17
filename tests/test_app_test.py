import unittest
from unittest.mock import patch
from flask.testing import FlaskClient

class TestAppTest(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config["TESTING"] = True
        self.client = self.app.test_client()

    def test_index(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Hello, World!"})

if __name__ == "__main__":
    unittest.main()
