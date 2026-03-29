from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")  # for WSl for not using GUI App

driver = webdriver.Chrome(options=options)

driver.get("https://www.google.com")

print("Title:", driver.title)

driver.quit()

# pipenv install selenium
# sudo apt install chromium-browser chromium-chromedriver

# chromedriver --version
#  which chromium
# pipenv shell
# python3 selenium-test.py