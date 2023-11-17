from selenium import webdriver
from selenium.webdriver.common.by import By
# Keep browser open after program finishes by getting a hold of Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")

price_dollar = driver.find_element(By.CLASS_NAME, "a-price-whole")
price_cents = driver.find_element(By.CLASS_NAME, "a-price-fraction")
print(f"{price_dollar.text}.{price_cents.text}")



# Close browser programmatically
# close() closes the particular tab
# driver.close()
# quit() closes the entire browser/program
driver.quit()
