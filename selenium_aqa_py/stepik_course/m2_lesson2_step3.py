from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://suninjuly.github.io/selects1.html"

browser = webdriver.Chrome()
browser.get(link)

x = browser.find_element(By.ID, "num1").text
y = browser.find_element(By.ID, "num2").text

x_y_sum = str(int(x) + int(y))

browser.find_element(By.TAG_NAME, "select").click()
browser.find_element(By.CSS_SELECTOR, f"[value='{x_y_sum}']").click()

button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
button.click()
