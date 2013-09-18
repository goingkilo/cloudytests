from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random

# Create a new instance of the Firefox driver
driverisat = './driver/chromedriver'
driver = webdriver.Chrome( driverisat )

driver.get("http://localhost:8080/login.html")

page1  = driver.find_element_by_name("user")
page1.send_keys("Cheese");
page1.submit()


gid = driver.find_element_by_name("login")
gpwd =driver.find_element_by_name("password") 

gid.send_keys('userid')
gpwd.send_keys('password')

ubmit = driver.find_element_by_name("commit");
ubmit.submit();
		

# the page is ajaxy so the title is originally this:
print driver.title

import time

#time.sleep(10)

runnote  = driver.find_element_by_partial_link_text('Run')

print 10*'#',runnote
	
css_of_new_notebook = 'div#editor-book-tree ul.tree li.folder ul li div span.title'
new_notebook = driver.find_element_by_css_selector( css_of_new_notebook )
new_notebook.click()

time.sleep(2)
filenode = driver.find_element_by_css_selector("div#editor-file-tree ul.tree li.folder ul li.folder ul")
files = filenode.find_elements_by_css_selector('li')
nf = len(files)-1
#newfile = driver.find_element_by_css_selector("div#editor-file-tree ul.tree li.folder ul li.folder ul li:nth-child('+nf+')")
#newfile.click()
files[len(files)-1].click()

filename = 'testfilename_' + str(random.randint(1,100))
print 10*'#' ,' file name generated :',filename

time.sleep(2)

alert = driver.switch_to_alert()
alert.send_keys(filename)
time.sleep(2)
alert.accept()


cmd = driver.find_element_by_id('new-md-cell-button')
cmd.send_keys('1 + 1')
cmd.send_keys(Keys.ENTER)
time.sleep(2)
cmd.send_keys('plot(iris)')
cmd.send_keys(Keys.ENTER)



try:
	n6  = driver.find_element_by_partial_link_text('New Note')
	print n6
except:
	print 'no partial link text'
	time.sleep(10)

time.sleep(10)
driver.quit()

"""
try:
    # we have to wait for the page to refresh, the last thing that seems to be updated is the title
    WebDriverWait(driver, 10).until(EC.title_contains("cheese!"))

    # You should see "cheese! - Google Search"
    print driver.title

finally:
    driver.quit()
"""

