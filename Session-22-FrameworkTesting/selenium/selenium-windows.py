from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://www.google.com')

print("Title: ", driver.title)

driver.quit()