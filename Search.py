# Import the Selenium 2 namespace (aka "webdriver")
from selenium import webdriver

# Google Chrome
driver = webdriver.Chrome('C:\dev\chromedriver_win32\chromedriver.exe')
driver.maximize_window()

# Go to ae.com
driver.get('https://www.ae.com')
driver.implicitly_wait(30)

# Search jeans
python_search = driver.find_element_by_name('search-input')
python_search.click()
python_search.send_keys("jeans")
python_search.send_keys(u'\ue007')

# Close the browser
driver.quit()