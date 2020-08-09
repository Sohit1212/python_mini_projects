from selenium import webdriver
#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Chrome()
driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
messageField = driver.find_element_by_xpath('//*[@id="user-message"]')
messageField.send_keys('Hello World')
showMessageButton = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div[2]/form/button')
showMessageButton.click()

value_a = driver.find_element_by_xpath('//*[@id="sum1"]')
value_a.send_keys(13)
value_b = driver.find_element_by_xpath('//*[@id="sum2"]')
value_b.send_keys(23)
sumButton = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div[2]/form/button')
sumButton.click()


#caps = DesiredCapabilities.FIREFOX.copy()
#caps['marionette'] = False
#caps["binary"] = '/usr/bin/firefox-bin'
#driver=webdriver.Firefox(capabilities=caps)
