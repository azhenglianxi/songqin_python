from selenium import webdriver
import time

def deleteAllCourse():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    driver.get("http://localhost/mgr/login/login.html")
    driver.find_element_by_id("username").send_keys("auto")
    driver.find_element_by_id("password").send_keys("sdfsdfsdf")
    driver.find_element_by_tag_name("button").click()

    driver.implicitly_wait(1)
    while True:
        deleteButtons = driver.find_elements_by_css_selector('button[ng-click="delOne(one)"]')
        if deleteButtons:
            deleteButtons[0].click()
            driver.find_element_by_css_selector('button.btn-primary').click()
            time.sleep(1)
        else:
            break
    driver.implicitly_wait(10)
    # deleteButton = driver.find_elements_by_css_selector('*[ng-click="delOne(one)"]')
    # for each in deleteButton:
    #     each.click()
    #     driver.find_element_by_css_selector('button.btn-primary').click()
    driver.quit()


# deleteAllCourse()

