#!/usr/bin/env python
#@Time     :2019-10-31 10:32:28   #@Author   :azhenglianxi   
#@Software :PyCharm

from Selenium_auto.funtion_Interface import *

#先登录到 51.job
driver =ChromeDriverBrowser()
driver.get('http://www.51job.com')
driver.implicitly_wait(10)
driver.find_element_by_id('kwdselectid').send_keys('python')
driver.find_element_by_id('work_position_click').click()   #打开城市定位搜索    #driver.find_element_by_css_selector('#work_position_click_center_right em')
district = driver.find_elements_by_css_selector('#work_position_click_center_right_list_000000 em[class=on]')
for one in district:
    one.click()
driver.find_element_by_id('work_position_click_center_right_list_category_000000_080200').click()#杭州这个城市的标签
driver.find_element_by_id('work_position_click_bottom_save').click()  #保存

driver.find_element_by_css_selector('.ush>button').click()  #搜索
reslist =driver.find_elements_by_css_selector('#resultList div.el')
for one in reslist:
    if 'title' in one.get_attribute('class'):
        continue
    fields =one.find_elements_by_tag_name('span')
    jobs_lists =[field.text for field in fields]
    print('||'.join(jobs_lists))

input()

driver.quit()

'''

driver.find_element_by_id('kwdselectid').send_keys('python')
# 点击工作地点
driver.find_element_by_id('work_position_input').click()


# 选择所有城市，去掉非杭州的且选择杭州，
# 如果是杭州但是没有选，选上这些城市
cityEles = driver.find_elements_by_css_selector('#work_position_click_center_right em')

for one in cityEles:
    cityName = one.text
    selected = one.get_attribute('class')
    # print cityName,seleted

    if cityName == u'杭州':
        if selected != 'on':
            one.click()

    else:
        if selected == 'on':
            one.click()

# 保存城市选择
driver.find_element_by_id('work_position_click_bottom_save').click()

# 点击搜索
driver.find_element_by_css_selector('.ush  button').click()

# 搜索结果分析
jobs = driver.find_elements_by_css_selector('#resultList  div.el')

for job in jobs:
    # 去掉第一行：标题行
    if 'title' in job.get_attribute('class'):
        continue

    filelds = job.find_elements_by_tag_name('span')
    strField = [fileld.text for fileld in filelds]
    print (' | '.join(strField))


driver.quit()
'''