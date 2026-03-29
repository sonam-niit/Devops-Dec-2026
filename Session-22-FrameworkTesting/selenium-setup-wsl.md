# Selenium Framework

- we can create simple selenium-test.py file which is just loading Google Chrome and test the website automatically.
- noramally selenium trying to test website from browsers but WSL doesn't allow this (GUI APP)
- so for managing that using webdriver of selenium with headless
- to run application in headless mode without opening chrome it will check the web application and execute test cases.

[WebDriver Manager](https://pypi.org/project/webdriver-manager/)
[Python Selenium](https://pypi.org/project/selenium/)

```py
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
```

### Work with Selenium in Windows

- download Python for Windows
- install with basic setup by just saying yes while installation
- once installed on terminal and check: python --version
- then go for selenium installtion: python -m pip install selenium

- create Driver Setup
- https://storage.googleapis.com/chrome-for-testing-public/147.0.7727.24/win64/chromedriver-win64.zip
- download from here
- extract and copy chromedrivet to C:/Drivers folder
- if fonder not exists create the Drivers folder

- then write below lines of code

```py
from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://www.google.com')

print("Title: ", driver.title)

driver.quit()
```

- just run in cmd: python selenium-windows.py
- you can see browser open automatically loads google.com
- check title in cmd
- and browser exis automatically.