#完成获取数据
from Selenium_auto.funtion_Interface import ChromeDrverNObroews
import time
from selenium import webdriver
url_weather="http://www.weather.com.cn/html/province/jiangsu.shtml"
#chrome_weBdriver='D:\\Users\\azhenglianxi\\AppData\\Local\\Programs\\Python\\Python37\\Scripts\\chromedriver.exe'
#登录浏览器
driver = ChromeDrverNObroews()
driver.get(url_weather)
#通过ID获取 文本
ele=driver.find_element('id','forecastID')
dls =ele.find_elements_by_tag_name('dl')
lowest =''
lowestCity =[]
#遍历打印
for one in dls:
    temp =one.text.split('\n')
    cityname =temp[0]
    lowweather=min(int(t.replace('℃','')) for t in temp[1].split('/'))

    if lowest==''or lowest>lowweather:
        lowest =lowweather
        lowestCity=[cityname]
    elif lowest==lowweather:
        lowestCity.append(cityname)
print(f"最低温度的城市有：{lowestCity},温度为：{lowest}℃")
driver.quit()












