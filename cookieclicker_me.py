from  selenium import webdriver
from selenium.webdriver.common.by import By
chrome_options = webdriver.ChromeOptions()
from  time import sleep, time
chrome_options.add_experimental_option("detach", True)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")

sleep(3)

language_button = driver.find_element(by=By.ID, value="langSelect-EN")
language_button.click()
sleep(2)
cookie = driver.find_element(By.ID, value="bigCookie")
for x in range(500):
    cookie.click()
grandma = driver.find_element(By.ID, value="product1")
grandma.click()

