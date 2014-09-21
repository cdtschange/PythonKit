#coding=utf-8
import ucenter.app
import unittest

class LoginTestCase(unittest.TestCase):
    
    def test_index(self):
        tester = ucenter.app.app.test_client(self)
        response = tester.get('/ucenter/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)
      
    def test_login_page_loads(self):
        tester = ucenter.app.app.test_client(self)
        response = tester.get('/ucenter/login', content_type='html/text')
        self.assertTrue(b'请登录' in response.data)  
        
    def test_correct_login(self):
        tester = ucenter.app.app.test_client(self)
        response = tester.post(
                    '/ucenter/login', 
                    data=dict(username='admin', password='admin'),
                    follow_redirects=True)
        self.assertTrue(b'已登录' in response.data)
        
    def test_incorrect_login(self):
        tester = ucenter.app.app.test_client(self)
        response = tester.post(
                    '/ucenter/login', 
                    data=dict(username='admin', password='wrong'),
                    follow_redirects=True)
        self.assertTrue(b'密码错误' in response.data)  
        
    
    def test_logout(self):
        tester = ucenter.app.app.test_client(self)
        response = tester.post(
                    '/ucenter/login', 
                    data=dict(username='admin', password='admin'),
                    follow_redirects=True)
        response = tester.get('/ucenter/logout', follow_redirects=True)
        self.assertTrue(b'已退出' in response.data)  

    
    def test_main_route_requires_login(self):
        tester = ucenter.app.app.test_client(self)
        response = tester.get('/', follow_redirects=True)
        self.assertTrue(b'登录' in response.data)  
        
if __name__ == '__main__':
    unittest.main()