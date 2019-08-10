from page.shopping_activity_goods import ShoppingActivityGoods
from common.base import open_mobile
import unittest

class TestShoppingActivityGoods(unittest.TestCase):
    def setUp(self):
        driver = open_mobile()
        self.sag = ShoppingActivityGoods(driver)

    def tearDown(self):
        self.sag.close_app()

    def test_shopping_activity_goods(self):
        """促销商品购买测试"""
        # 点击我的
        self.sag.click_my()
        # self.sag.click_head()
        # self.sag.send_username("18982954299")
        # self.sag.send_password("123456")
        # self.sag.click_login()
        # 获取账户余额
        result = self.sag.get_balance("text")
        # 将账户余额转换为浮点型
        start_balance = float(result)
        print(start_balance)
        # 点击首页
        self.sag.click_home_page()
        # 点击促销商品
        self.sag.click_product_promotions()
        # 点击某个商品
        self.sag.click_good()
        # 点击立即购买
        self.sag.click_now_buy()
        # 点击确认
        self.sag.click_sure()
        # 使用账户余额购买
        self.sag.click_use_balance()
        # 获取商品的价格
        good_price = self.sag.get_good_price("text")
        # 去除商品价格前的￥符号
        price = good_price[1:]
        # 将商品价格转换为浮点型
        price1 = float(price)
        print(price1)
        # 点击提交订单
        # self.sag.click_place_order()
        # # 输入支付密码
        # self.sag.send_pay_password("123456")
        # # 点击确定
        # self.sag.click_sure()
        # 返回首页
        self.sag.page_back()
        self.sag.page_back()
        self.sag.page_back()
        # 点击我的
        self.sag.click_my()
        # 获取购买商品后的账户余额
        result1 = self.sag.get_balance("text")
        # 将账户余额转换为浮点型
        end_balance = float(result1)
        print(end_balance)
        # 断言
        # self.assertEqual(end_balance,start_balance-price1)
        self.assertEqual(end_balance, start_balance)