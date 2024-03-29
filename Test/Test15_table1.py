from selenium import webdriver
import time
import os

# start webdriver and load website from disk
driver = webdriver.Chrome()
url = 'file:///' + os.getcwd() + '/websites/table.html'
driver.get(url)
time.sleep(1)

# select table
table = driver.find_element_by_id('table')

# iterate through table
rows = table.find_elements_by_tag_name("tr")

# get row
for row in rows:
    if len(row.find_elements_by_tag_name("td")) > 0:
        col = row.find_elements_by_tag_name("td")[1]
        print(col.text)

time.sleep(3)
driver.quit()

