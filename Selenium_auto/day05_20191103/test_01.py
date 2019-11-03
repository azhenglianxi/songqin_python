#!/usr/bin/env python
#@Time     :2019-11-01 21:09:01   #@Author   :azhenglianxi   
#@Software :PyCharm



xpath = "//标签名[@属性='属性值']"





#  //*[@id="food"]/*[position()<=3]


#//*[@id="food"]/*[position()>=last()-1]


#//*[@id="food"]/*[position()>last()-2]

#//*[@id='food']/*[position()>1 and position() < 4]这样也可以吧


#following-sibling::   #相邻元素

#//*[@id='food']/preceding-sibling::p  前面的元素
#//*[@id='food']/preceding-sibling::div[position()>=last()-1]


#//*[@id='food']/following-sibling::p[position()>=last()-1]  取离他最远的两个元素

# xpath  通过子元素 找到父元素
#//a[@id=='3']/.."

