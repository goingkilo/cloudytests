from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By

# Create a new instance of the Firefox driver
driverisat = '/home/kraghu/testing/selenium/webdriver/chromedriver'
driver = webdriver.Chrome( driverisat )

driver.get("http://localhost:8080/login.html")

page1  = driver.find_element_by_name("user")
page1.send_keys("Cheese");
page1.submit()


gid = driver.find_element_by_name("login")
gpwd =driver.find_element_by_name("password") 

gid.send_keys('github id')
gpwd.send_keys('github password')

ubmit = driver.find_element_by_name("commit");
ubmit.submit();
		

# the page is ajaxy so the title is originally this:
print driver.title

import time

time.sleep(10)

n6  = driver.find_element_by_partial_link_text('a6')

print n6

"""
try:
    # we have to wait for the page to refresh, the last thing that seems to be updated is the title
    WebDriverWait(driver, 10).until(EC.title_contains("cheese!"))

    # You should see "cheese! - Google Search"
    print driver.title

finally:
    driver.quit()
"""
