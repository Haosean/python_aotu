# coding = utf-8
# print '1122'
from selenium import webdriver
import time

browser = webdriver.Chrome()
# browser = webdriver.Chrome()
url = 'http://10.1.0.52/middlecas/login?service=http://10.1.0.52:8080/middleresource/shiro-cas'
print "now access %s" % (url)
browser.get(url)

time.sleep(2)
# browser.find_element_by_id("kw").send_keys("selenium")
# browser.find_element_by_id("su").click()
# time.sleep(3)
# browser.quit()
select = browser.find_element_by_tag_name("select")
allOptions = select.find_elements_by_tag_name("option")
# for option in allOptions:
#    print "Value is: " + option.get_attribute("value")
for option in allOptions:
    if option.get_attribute('value') == 'd665c05e-9ff9-414d-84bd-9cbc099cbdfd':
        option.click()
time.sleep(2)

browser.find_by_id('s_username').fill('administrator')
browser.find_by_id('s_password').fill('xungejiaoyu')
browser.find_by_name('submit').click()

time.sleep(8)
# close the window of brower
browser.quit()
# for input in inputs:
#    if input.get_attribute('type') == 'checkbox':
#        input.click()
# time.sleep(2)
