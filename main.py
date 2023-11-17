from selenium import webdriver
from selenium.webdriver.common.by import By
# Keep browser open after program finishes by getting a hold of Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")
# driver.get("https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")
#
# price_dollar = driver.find_element(By.CLASS_NAME, "a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, "a-price-fraction")
# print(f"{price_dollar.text}.{price_cents.text}")

# Find element by attribute NAME
search_bar = driver.find_element(By.NAME, value='q')
# This just prints out a Selenium element
print(search_bar)
# Get tag name
print(search_bar.tag_name)
# Get attribute
print(search_bar.get_attribute("placeholder"))

# Find element by attribute ID
button = driver.find_element(By.ID, value='submit')
# Get hold of various properties of the element like size
print(button.size)

# if an element doesn't have an attribute/class/id find its parent's attribute/class/id
# then find element by CSS selector
documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(documentation_link.text)

# if all else fails use the xpath to find the element
bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)
print(bug_link.get_attribute("href"))


# Close browser programmatically
# close() closes the particular tab
# driver.close()
# quit() closes the entire browser/program
driver.quit()
