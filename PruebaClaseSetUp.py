from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class TestMoodle(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()	
        cls.driver.get("https://accounts.google.com/ServiceLogin")
    
    def test_login_mail(self):
        user = self.driver.find_element_by_id("Email")
        passwd = self.driver.find_element_by_id("Passwd-hidden")
        user.send_keys("dr.raigoza@gmail.com")
        self.driver.send_keys(Keys.RETURN)
        passwd.end_keys(u"weedness123")
        self.driver.send_keys(Keys.RETURN)
    # Diferencia entre setup metodo y clase, la clase permite realizar las pruebas sin tener que abrir cada prueba el explorador
    @classmethod
    def teatDownClass(cls):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
