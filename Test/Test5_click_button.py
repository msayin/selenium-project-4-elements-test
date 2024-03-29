from selenium import webdriver
import time
import os

# start webdriver and load website from disk
driver = webdriver.Chrome()
url = 'file:///' + os.getcwd() + '/websites/button.html'
driver.get(url)
time.sleep(1)

# click button
python_button = driver.find_element_by_xpath("//button[contains(text(),'Click Me!')]")
python_button.click()

# close javascript popup
time.sleep(3)
alert = driver.switch_to_alert()
alert.accept()

time.sleep(5)
driver.quit()