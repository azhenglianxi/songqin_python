from selenium import webdriver
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.implicitly_wait(10)

driver.get('https://kyfw.12306.cn/otn/leftTicket/init')

#输入起点和终点
ele=driver.find_element_by_id('fromStationText')
ele.click()
ele.send_keys('南京南\n')

ele1=driver.find_element_by_id('toStationText')
ele1.click()
ele1.send_keys('杭州东\n')

#选择发车时段
select=Select(driver.find_element_by_id('cc_start_time'))
select.select_by_visible_text('06:00--12:00')

#选择发车时间-当前日期的第二天
driver.find_element_by_xpath('//*[@id="date_range"]//li[2]').click()

xpath='//*[@id="queryLeftTable"]//td[4][@class]/preceding-sibling::td[last()]//a'

xpath2='//*[@id="queryLeftTable"]//td[4][@class]/../td[1]//a'

trains=driver.find_elements_by_xpath(xpath2)

print('二等座有座的车次有：')
for t in trains:
    print(t.text)

driver.quit()


#//*[@id="queryLeftTable"]/tr/td[4][@class]/preceding-sibling::td[last()]
# //*[@id="queryLeftTable"]/tr/td[4][@class]/../td[1]
#//*[@id="queryLeftTable"]/tr/td[4][@class]/../td[1]//a