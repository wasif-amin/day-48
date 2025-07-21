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
products = driver.find_elements(By.CSS_SELECTOR, value="div[id^='product']")
elements = []
grandma = None
#----------------------why does this work----------- ⬇️
for product in products:
    if "enabled" in product.get_attribute("class"):
        price = product.text.split("\n")[1]
        int_price = int(price)
        if int_price == 100:
            grandma = product
            break
if grandma:
    grandma.click()
#------------ but not this ------- ⬇️
# for current_product_webElement in products:
#     if "enabled" in current_product_webElement.get_attribute("class"):
#         elements.append(current_product_webElement.text)
# for element in elements:
#     price = element[0]
#     int_price = int(price)
#     if 100 in int_price:
#         grandma = current_product_webElement
#         break
# if grandma:
#    grandma.click()

