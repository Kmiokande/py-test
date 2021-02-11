import unittest
from app import web_app


class TestHomeView(unittest.TestCase):
    def setUp(self):
        app = web_app.test_client()
        self.response = app.get('/')

    def test_get(self):
        self.assertEqual(self.response.status_code, 200)

    def test_html_string_response(self):
        self.assertEqual("ok", self.response.data.decode('utf-8'))

    def test_content_type(self):
        self.assertIn('text/html', self.response.content_type)
