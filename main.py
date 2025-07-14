from  selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
#chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")


# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"the price is {price_dollar.text}.{price_cents.text}")
#
#search_bar =  driver.find_element(By.NAME, value="q")
#print(search_bar.get_attribute("placeholder"))
# button = driver.find_element(By.ID, value="submit")
# print(button)
# docs_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a ")
# print(docs_link.text)


# x = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]/a')
# print(x.text)
x = driver.find_element(By.CSS_SELECTOR, value=".event-widget li a")
print(x.text)










# bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)





# event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
# event_names  = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
# events = {}
# for n in range(len(event_times)):
#     events[n] ={
#         "time": event_times[n].text,
#             "name": event_names[n].text
#     }
# print(events)
# # driver.close(
driver.quit()
