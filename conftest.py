# 导包
from appium import webdriver
import pytest


@pytest.fixture(autouse=True)
def open_mobile():
    # 配置启动参数
    desired_caps = {}
    # 指定系统名称
    desired_caps["platformName"] = "android"
    # 指定系统版本
    desired_caps["platformVersion"] = "5.1.1"
    # 指定设备名称
    desired_caps["deviceName"] = "127.0.0.1:21503"
    # 指定APP包名
    desired_caps["appPackage"] = "com.tpshop.malls"
    # 指定APP启动名
    desired_caps["appActivity"] = ".SPMainActivity"
    # 启用Unicode输入法，设置为true可以输入中文字符
    desired_caps['unicodeKeyboard'] = True
    # 在设定了`unicodeKeyboard`关键字运行Unicode测试结束后，将键盘重置为其原始状态
    desired_caps['resetKeyboard'] = True
    # 不重置应用
    desired_caps["noReset"] = True
    # 打开手机APP
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
    return driver
