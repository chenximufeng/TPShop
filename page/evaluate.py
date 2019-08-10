import time

from common.base import Base
from common.base import open_mobile

class Evaluate(Base):
    my_locator = ("xpath", '//*[@text="我的"]')
    head_locator = ("id", "com.tpshop.malls:id/head_img")
    username_locator = ("xpath", '//*[@text="请输入账号"]')
    password_locator = ("id", "com.tpshop.malls:id/pwd_et")
    login_locator = ("id", "com.tpshop.malls:id/login_tv")
    home_page_locator = ("xpath", '//*[@text="首页"]')
    wait_evaluate_locator = ("xpath", '//*[@text="待评价"]')
    evaluate_locator = ("id","com.tpshop.malls:id/order_show_btn")
    evaluate_content_locator = ("id","com.tpshop.malls:id/comment_content_et")
    button_locator = ("id","com.tpshop.malls:id/anonymous_rb")
    grade_locator = ("id","com.tpshop.malls:id/star1_btn")
    submit_locator = ("xpath", '//*[@text="提交"]')
    good_name_locator = ("id","com.tpshop.malls:id/product_name_tv")


    def click_my(self):
        """点击我的"""
        self.click(self.my_locator)

    def click_head(self):
        """点击头像"""
        self.click(self.head_locator)

    def send_username(self,username):
        """输入用户名"""
        self.send_keys(self.username_locator,username)

    def send_password(self,password):
        """输入密码"""
        self.send_keys(self.password_locator,password)

    def click_login(self):
        """点击登录"""
        self.click(self.login_locator)

    def click_home_page(self):
        """点击首页"""
        self.click(self.home_page_locator)

    def wait_evaluate(self):
        """点击待待评价"""
        self.click(self.wait_evaluate_locator)

    def click_evaluate(self):
        """点击评价晒单"""
        self.click(self.evaluate_locator)

    def send_evaluate_content(self,content):
        """输入评价内容"""
        self.send_keys(self.evaluate_content_locator,content)

    def grade_evaluate(self,num):
        """星级评价"""
        self.click_all_element(self.grade_locator,num)

    def click_submit_button(self):
        """点击提交"""
        self.click(self.submit_locator)

    def get_good_name(self,content):
        """获取评价的商品名称"""
        return self.get_element_text(self.good_name_locator,content)

    def get_all_goods_name(self):
        """获取所有商品名称"""
        elements = self.find_elements(self.good_name_locator)
        goods_name = []
        for element in elements:
            # 获取元素文本
            name = element.get_attribute("text")
            goods_name.append(name)
        # goods_name = self.get_elements_text(self.all_goods_name_loc)
        # print(goods_name)
        return goods_name

    def click_already_evaluate(self):
        """点击已评价"""
        self.by_coordinate_click_element(x=429,y=107)

    def good_name_is_already_evaluate(self, good_name):
        """判断评价的商品是否存在已评价的列表里"""
        all_goods_name = self.get_all_goods_name()
        if good_name in all_goods_name:
            return True
        else:
            print("您添加的商品不存在!")
            return False


if __name__ == '__main__':
    driver = open_mobile()
    ev = Evaluate(driver)
    # 点击我的
    ev.click_my()
    # 点击待评价
    ev.wait_evaluate()
    time.sleep(3)
    # 点击已评价
    ev.click_already_evaluate()
    print(ev.get_all_goods_name())
    # result = ev.get_good_name("text")
    # print(result)
    # ev.click_evaluate()
    # ev.send_evaluate_content("很好！非常好！")
    # ev.grade_evaluate(0)
    # ev.grade_evaluate(1)
    # ev.grade_evaluate(2)
    # ev.grade_evaluate(3)
    # ev.click_submit_button()
    # result1 = ev.get_good_name("text")
    # print(result1)

