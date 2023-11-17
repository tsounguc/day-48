from selenium import webdriver
# Keep browser open after program finishes by getting a hold of Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com")

# Close browser programmatically
# close() closes the particular tab
# driver.close()
# quit() closes the entire browser/program
# driver.quit()
