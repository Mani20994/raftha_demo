from selenium import webdriver
import time

driver = webdriver.Chrome("C:\\Users\\nxt222\\PycharmProjects\\TestAutomation\\Drivers\\chromedriver.exe")
driver.set_page_load_timeout(20)
driver.get("https://www.facebook.com")

driver.maximize_window()

driver.quit()
