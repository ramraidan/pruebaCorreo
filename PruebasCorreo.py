from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class TestGooglePage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://mail.google.com/mail/')
    
    def test_login_gmail(self):
        login = self.driver.find_element_by_id('Email')
        login.send_keys("dr.raigoza@gmail.com")
        login.send_keys(Keys.RETURN)
        passwd = self.driver.find_element_by_class('Hidden')
        passwd.send_keys("password")
        passwd.send_keys(Keys.RETURN)
        time.sleep(25)
        correo = self.driver.find_element_by_class('yP')
        correo.click()
		self.assertEqual('Notificación',self.driver.title)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()