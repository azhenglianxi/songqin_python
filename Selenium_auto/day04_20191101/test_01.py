#!/usr/bin/env python
#@Time     :2019-11-01 21:09:01   #@Author   :azhenglianxi   
#@Software :PyCharm

"""
1）概述：可以根据元素的属性及属性值来选择元素

2）语法：[属性=”属性值”]; 星号表示任意元素标签名; 通常属性值没有空格或特殊字符可以不加引号

3）实例：*[style]

4）使用场景：选择具有某个属性（值）的元素




"""
#选择id为many下某(name)属性的所有元素

#ele=driver.find_elements_by_css_selector('#many p[name]')
#for one in ele:
  #  print(one.text)


# 选择特定的元素
# ①单属性匹配元素：p[属性=”属性值”]
#
# ②多属性匹配元素：p[属性=”属性值”][属性=”属性值”]
#
# ③=表示属性值完全匹配

#ele=driver.find_element_by_css_selector('#many p[name="p1"]')#方法1
#ele=driver.find_element_by_css_selector('#many p[name="p1"][class="special"]')#方法2
#print(ele.text)

# 三、元素属性定位
#
# （1）input[id=kw]
#
# （2）input[class=s_ipt]
#
# （3）input[id=kw][class=s_ipt]
#
# 还支持模糊匹配的，主要是太长的属性值方便使用；以class=bg s_ipt_wr quickdelete-wrap举例：
#
# （1）span[class ^=bg]    匹配所有span标签class属性值bg开头的元素
#
# （2）span[class $=rap]    匹配所有span标签class属性值rap结尾的元素
#
# （3）span[class *=quick]    匹配所有span标签class属性值中间有quick的元素

#
# （1）first-child：第一个后代元素
#
# （2）last-child：最后一个后代元素
#
# （3）nth-child(N)：指定第N个后代元素