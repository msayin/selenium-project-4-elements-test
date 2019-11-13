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

# get header rows
headers = rows[0].find_elements_by_tag_name("th")
for header in headers:
    print(header.text)


fruits = []
countries = []

# get row
for row in rows:
    if len(row.find_elements_by_tag_name("td")) > 0:
        fruits.append( row.find_elements_by_tag_name("td")[0].text )
        countries.append( row.find_elements_by_tag_name("td")[1].text )

print(fruits)
print(countries)

time.sleep(3)
driver.quit()

