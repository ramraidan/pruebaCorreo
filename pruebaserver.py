from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys

driver = webdriver.Remote(
   command_executor='http://127.0.0.1:4444/wd/hub',
   desired_capabilities=DesiredCapabilities.FIREFOX)

driver.get("http://ingsoftware.reduaz.mx/moodle/login/index.php")
print (driver.title)

user = driver.find_element_by_id("username")
passw = driver.find_element_by_id("password")

user.send_keys("usuario")
passw.send_keys("pass")
passw.send_keys(Keys.RETURN)
