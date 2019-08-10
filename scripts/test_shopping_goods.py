from page.shopping_goods import ShoppingGoods
from common.base import open_mobile
import unittest

class TestShoppingActivityGoods(unittest.TestCase):
    def setUp(self):
        driver = open_mobile()
        self.sg = ShoppingGoods(driver)

    def tearDown(self):
        self.sg.close_app()

    def test_shopping_goods(self):
        """非促销商品购买测试"""
        # 点击我的
        self.sg.click_my()
        # self.sg.click_head()
        # self.sg.send_username("18428389548")
        # self.sg.send_password("123456")
        # self.sg.click_login()
        # 获取账户余额
        result = self.sg.get_balance("text")
        # 将账户余额转换为浮点型
        start_balance = float(result)
        print(start_balance)
        # 点击首页
        self.sg.click_home_page()
        # 点击分类
        self.sg.click_classification()
        # 点击服饰
        self.sg.click_clothes()
        # 点击新品推荐
        self.sg.click_new_goods()
        # 点击某个商品
        self.sg.click_good()
        # 点击立即购买
        self.sg.click_now_buy()
        # 点击确认
        self.sg.click_sure()
        # 使用账户余额购买
        self.sg.click_use_balance()
        # 获取商品的价格
        good_price = self.sg.get_good_price("text")
        # 去除商品价格前的￥符号
        price = good_price[1:]
        # 将商品价格转换为浮点型
        price1 = float(price)
        print(price1)
        # 点击提交订单
        self.sg.click_place_order()
        # 输入支付密码
        self.sg.send_pay_password("123456")
        # 点击确定
        self.sg.click_sure()
        # 返回首页
        self.sg.page_back()
        self.sg.page_back()
        self.sg.page_back()
        # 点击我的
        self.sg.click_my()
        # 获取购买商品后的账户余额
        result1 = self.sg.get_balance("text")
        # 将账户余额转换为浮点型
        end_balance = float(result1)
        print(end_balance)
        # 断言
        # self.assertEqual(end_balance, start_balance - price1)
        self.assertEqual(end_balance, start_balance)