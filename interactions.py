from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

num =  driver.find_element(By.XPATH, value='//*[@id="articlecount"]/ul/li[2]/a[1]')
num_from_id = driver.find_element(By.ID, value="articlecount")
portals = driver.find_element(By.LINK_TEXT, value="Content portals")
search = driver.find_element(By.CLASS_NAME, value="cdx-text-input__input")
search.send_keys("python")
search.send_keys(Keys.ENTER)
