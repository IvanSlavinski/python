from selenium import webdriver
from selenium.webdriver.common.by import By
import math

link = "http://SunInJuly.github.io/execute_script.html"

browser = webdriver.Chrome()
browser.get(link)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


x = int(browser.find_element(By.ID, "input_value").text)
y = calc(x)

input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
input1.send_keys(y)

option1 = browser.find_element(By.CSS_SELECTOR, ".form-check-input:nth-child(1)")
option1.click()

option2 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
option2.click()

button = browser.find_element(By.TAG_NAME, "button")
button.click()
