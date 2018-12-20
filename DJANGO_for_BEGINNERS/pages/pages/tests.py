from django.test import TestCase, SimpleTestCase

# Create your tests here.
class SimpleTest(SimpleTestCase):
    
    # HttpRequestに対してリクエスト成功(=200)の応答が返ってきていることを確認するテスト
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200) 
    
    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
