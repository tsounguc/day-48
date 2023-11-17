from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Instantiate options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Instantiate driver
driver = webdriver.Chrome(options=chrome_options)

# Open website
driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element(By.CSS_SELECTOR,'#articlecount a')
print(article_count.text)

# article_count.click()

view_history = driver.find_element(By.LINK_TEXT, "View history")
view_history.click()

search_button = driver.find_element(By.CSS_SELECTOR, "#p-search a")
search_button.click()

search_bar = driver.find_element(By.NAME, "search")
search_bar.send_keys("Python")

search_bar = driver.find_element(By.NAME, "search")
search_bar.send_keys(Keys.ENTER)



# close website
# driver.quit()
