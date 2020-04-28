import pytest
def test_01():
    print("sadsadsadsa")

# 初始化操作
def setup():
    pass

def teardown():
    pass



# pytest # run all tests below current dir  + -s 可以进行输入和输出
# # 在当前测试文件的目录下，寻找以test开头的文件（即测试文件），找到测试文件之后，进入到测试文件中寻找test_开头的测试函数并执行
#
#
# pytest test_mod.py # run tests in module     #执行某一个指定的测试文件
# pytest somepath # run all tests below somepath    #运行某一个目录下的所有测试用例#

# pytest-html 生成测试报告  安装产假 install pytest——html
# 指定报告格式及路径  pytest xxx.py --html =report.html
#  报告独立显示 pytest --html =report.html --self-contained-html