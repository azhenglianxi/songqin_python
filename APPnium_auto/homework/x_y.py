def taptest(driver):
    # 设定系数,控件在当前手机的坐标位置除以当前手机的最大坐标就是相对的系数了
    a1 = 188.8/1069
    b1 = 941.5/1916
    # 获取当前手机屏幕大小X,Y
    X = driver.get_window_size()['width']
    Y = driver.get_window_size()['height']
    # 屏幕坐标乘以系数即为用户要点击位置的具体坐标
    driver.tap([(a1*X, b1*Y)])
