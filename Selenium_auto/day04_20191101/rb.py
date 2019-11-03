# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By

executable_path = r"d:\tools\webdrivers\chromedriver.exe"
driver = webdriver.Chrome(executable_path)

driver.get('file:///D:/Users/azhenglianxi/songqin_python/Selenium_auto/day04_20191101/b.html')

driver.find_element_by_css_selector('[value="male"]').click()



driver.find_element_by_css_selector('[value="female"]').click()


driver.find_element_by_css_selector('[value="female"]').click()


# selected=driver.find_element_by_css_selector('[value="male"]').is_selected()

# print(selected)













# 这里使用了根据属性值来查找
# input1 = driver.find_element_by_css_selector("input[value=other]")
# input1.click()


# input('press any key to quit...')
driver.quit()   # 浏览器退出