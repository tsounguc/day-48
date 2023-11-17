from selenium import webdriver
from selenium.webdriver.common.by import By

# Instantiate options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Instantiate driver
driver = webdriver.Chrome(options=chrome_options)

# Open website
driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element(By.CSS_SELECTOR,'#articlecount a')
print(article_count.text)


# close website
driver.quit()
