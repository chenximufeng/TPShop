import time

from page.evaluate import Evaluate
from common.base import open_mobile
import unittest

class TestEvaluate(unittest.TestCase):
    def setUp(self):
        """开启app"""
        driver = open_mobile()
        self.ev = Evaluate(driver)

    def tearDown(self):
        """关闭app"""
        self.ev.close_app()

    def test_evaluate(self):
        """商品评价测试"""
        # 点击我的
        self.ev.click_my()
        # 点击头像
        self.ev.click_head()
        # 输入用户名
        self.ev.send_username("17788888888")
        # 输入密码
        self.ev.send_password("123456")
        # 点击登录
        self.ev.click_login()
        # 单机待评价
        self.ev.wait_evaluate()
        # 获取评价商品名称
        result = self.ev.get_good_name("text")
        print(result)
        # 点击评价晒单
        self.ev.click_evaluate()
        # 输入评价内容
        self.ev.send_evaluate_content("很好！非常好！")
        # 星级评价
        self.ev.grade_evaluate(0)
        self.ev.grade_evaluate(1)
        self.ev.grade_evaluate(2)
        self.ev.grade_evaluate(3)
        # 提交评价
        self.ev.click_submit_button()
        time.sleep(3)
        # 点击已评价
        self.ev.click_already_evaluate()
        # 判断评价的商品名称是否在已评价的列表中
        result1 = self.ev.good_name_is_already_evaluate(result)
        # result1 = self.ev.get_good_name("text")
        # print(result1)
        # 进行断言
        self.assertEqual(True,result1)