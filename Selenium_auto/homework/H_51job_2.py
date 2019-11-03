#!/usr/bin/env python
#@Time     :2019-10-31 10:32:28   #@Author   :azhenglianxi   
#@Software :PyCharm

from Selenium_auto.funtion_Interface import *
import  time
#先登录到 51.job
driver =ChromeDriverBrowser()
driver.get('http://www.51job.com')
driver.implicitly_wait(3)
#打开高级搜索
driver.find_element_by_xpath("//a[@class='more']").click()
#输入搜索关键词  python
driver.find_element_by_id('kwdselectid').send_keys('python')
#地区选择 杭州
driver.find_element_by_id('work_position_input').click()
#取消 反选城市
eles =driver.find_elements_by_xpath("//*[@id ='work_position_click_multiple_selected']/span")
for one in eles:
    one.click()
time.sleep(3)
# 选杭州
driver.find_element_by_id('work_position_click_center_right_list_category_000000_080200').click()
# 保存选择
driver.find_element_by_id('work_position_click_bottom_save').click()
# 要点一下别的地方， 否则下面的元素会被挡住
driver.find_element_by_xpath("//*[@id='saveSearchForm']/following-sibling::div[1]/label").click()
# 职能类别 选 计算机软件 -> 高级软件工程师
driver.find_element_by_id('funtype_click').click()
driver.find_element_by_id('funtype_click_center_right_list_category_0100_0100').click()
driver.find_element_by_id('funtype_click_center_right_list_sub_category_each_0100_0106').click()
driver.find_element_by_id('funtype_click_bottom_save').click()
time.sleep(2)
#公司性质选  外资欧美

driver.find_element_by_id('cottype_list').click()
time.sleep(1)

driver.find_element_by_xpath("//span[@title= '外资（欧美）']").click()
#工作年限选 1 - 3
driver.find_element_by_id('workyear_list').click()
time.sleep(1)
driver.find_element_by_xpath("//span[@title= '1-3年']").click()
driver.find_element_by_xpath("//div[@class='btnbox p_sou']/span[@class='p_but']").click()
#/html/body/div[2]/div[2]/div[10]/span
#搜索列表进行 结果搜索
reslist =driver.find_elements_by_css_selector('#resultList div.el')
for one in reslist[1:]:
   # if 'title' in one.get_attribute('class'):
   #     continue
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