from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from Selenium_auto.funtion_Interface import *
driver = ChromeDriverBrowser()
driver.implicitly_wait(10)

driver.get('https://www.vmall.com/')

#进入华为官网
driver.find_element_by_css_selector('a[href="http://consumer.huawei.com/cn/"]').click()
main_handle=driver.current_window_handle

#切换新窗口
for handle in driver.window_handles:
    driver.switch_to.window(handle)
    if '华为消费者业务官网' in driver.title:
        break

#查看菜单
menus=driver.find_elements_by_css_selector('li.nav-list')
menus=[m.text for m in menus]

expect='''  智能手机
  笔记本
  平板
  穿戴设备
  智能家居
  更多产品
  软件应用
  服务与支持'''

expects=[m.strip() for m in expect.splitlines()]
if expects==menus:
    print('pass')
else:
    print('fail')
    print(menus)

#回到主页
driver.switch_to.window(main_handle)

#鼠标停留菜单
action=ActionChains(driver)

action.move_to_element(driver.find_element_by_id('zxnav_1')).perform()

menus2=driver.find_elements_by_css_selector('#zxnav_1 ul>li')
menus2=[m.text for m in menus2]
print(menus2)

expect2="平板电脑|笔记本电脑|笔记本配件"
if expect2=='|'.join(menus2[:-1]):
    print('success')
else:
    print('fail')
    print(menus2)


driver.quit()





