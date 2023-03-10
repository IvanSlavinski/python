from selenium import webdriver
from selenium.webdriver.common.by import By
import math

link = "http://suninjuly.github.io/get_attribute.html"

browser = webdriver.Chrome()
browser.get(link)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


x_element = browser.find_element(By.CSS_SELECTOR, "#treasure")
x = x_element.get_attribute("valuex")
y = calc(x)

input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
input1.send_keys(y)

option = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
option.click()

option1 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
option1.click()

button = browser.find_element(By.CLASS_NAME, "btn-default")
button.click()
