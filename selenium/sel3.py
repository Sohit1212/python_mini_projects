from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://www.google.com/intl/en_in/earth/')

wait = WebDriverWait(driver,10)
launchButton = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/header/div/nav[1]/ul[2]/li[2]/a/span/span')))
launchButton.click()
