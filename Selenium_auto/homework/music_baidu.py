#!/usr/bin/env python
#@Time     :2019-10-29 14:50:04   #@Author   :azhenglianxi   
#@Software :PyCharm

from Selenium_auto.funtion_Interface import *
driver =ChromeDrverNObroews()
driver.get('http://music.baidu.com/top/new')
div =driver.find_element_by_id('songListWrapper')
ul =div.find_element_by_tag_name('ul')
li =ul.find_elements_by_tag_name('li')
for one in li:
    if one.find_elements_by_class_name('up'):
        music_titiel =one.find_element_by_class_name('song-title ').text
        author_list =one.find_element_by_class_name('author_list').text
        print(f'排名上升的歌曲有<<{music_titiel}>>,作者是 * {author_list}* ')
    elif one.find_elements_by_class_name('dowm'):
        music_titiel = one.find_element_by_class_name('song-title ').text
        author_list = one.find_element_by_class_name('author_list').text
        print(f'排名下升的歌曲有<<{music_titiel}>>,作者是 * {author_list}* ')
    else:
        music_titiel = one.find_element_by_class_name('song-title ').text
        author_list = one.find_element_by_class_name('author_list').text
        print(f'排名未变动的歌曲有<<{music_titiel}>>,作者是 * {author_list}* ')

input('.....')
driver.close()
driver.quit()
