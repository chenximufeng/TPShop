# 导包
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions  as EC
from selenium.webdriver.support.ui import Select
from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver

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

# 创建一个Base类
class Base(object):
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, timeout=5):
        """
        定位某个元素
        :param locator: 定位器
        :param timeout: 最长等待时间
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        except:
            return False
        else:
            return element

    def find_elements(self, locator, timeout=5):
        """定位一组元素"""
        try:
            elements = WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
        except:
            return False
        else:
            return elements

    def click(self, locator, timeout=5):
        """点击某个元素"""
        element = self.find_element(locator, timeout)
        element.click()

    def by_coordinate_click_element(self,x,y):
        """通过坐标点击元素"""
        TouchAction(self.driver).tap(x=x, y=y).perform()

    def click_all_element(self, locator, num, timeout=5):
        """点击所有元素"""
        elements = self.find_elements(locator, timeout)
        elements[num].click()

    def send_keys(self, locator, text, timeout=5):
        """ 在输入框中输入内容"""
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    def get_element_text(self,locator,content):
        """获取元素文本内容"""
        element = self.find_element(locator)
        result = element.get_attribute(content)
        return result

    def is_text_in_element(self, locator, text, timeout=5):
        """判断文本内容是否存在元素中"""
        try:
            result = WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator, text))
        except:
            print(f"{locator}元素未找到")
            return False
        else:
            return result

    def is_value_in_element(self, locator, value, timeout=5):
        """判断value属性值是否存在元素中"""
        element = self.find_element(locator, timeout)
        try:
            value1 = element.get_attribute("value")
            if value1 == value:
                return True
            else:
                return False
        except:
            return False

    def screen_shot(self, file_path):
        """
        截屏
        :param file_path: 存放截屏的路径
        """
        self.driver.get_screenshot_as_file(file_path)

    def select(self, locator, index, timeout=10):
        """
        下拉菜单旋选择
        :param locator: 定位器
        :param index: 索引值
        :param timeout: 最长等待时间
        """
        element = self.find_element(locator, timeout)
        select = Select(element)
        select.select_by_index(index)

    # 弹窗确认处理
    def alert_accept(self):
        alert = self.driver.switch_to.alert
        alert.accept()

    # 弹窗取消处理
    def alert_dismiss(self):
        alert = self.driver.switch_to.alert
        alert.dismiss()

    # 关闭APP
    def close_app(self):
        self.driver.quit()

    def get_elements_text(self, locator):
        """获取元素文本内容"""
        elements = self.find_elements(locator)
        text_list = []
        for element in elements:
            _text = element.text
            text_list.append(_text)
        return text_list

    def page_forward(self):
        """页面前进"""
        self.driver.forward()

    def page_back(self):
        """页面后退"""
        self.driver.back()

    def page_refresh(self):
        """刷新页面"""
        self.driver.refresh()

    def up_slide(self):
        """向下滑动"""
        self.driver.swipe(0, 927, 0, 138, duration=5000)

    def down_slide(self):
        """向下滑动"""
        self.driver.swipe(0, 138, 0, 927, duration=5000)

    def left_slide(self):
        """向左滑动"""
        self.driver.swipe(572, 0, 0, 0, duration=5000)

    def right_slide(self):
        """向右滑动"""
        self.driver.swipe(0, 0, 572, 0, duration=5000)
