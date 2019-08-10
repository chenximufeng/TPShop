from common.base import Base
from appium.webdriver.common.touch_action import TouchAction
from common.base import open_mobile

class ShoppingActivityGoods(Base):
    my_locator = ("xpath",'//*[@text="我的"]')
    head_locator = ("id","com.tpshop.malls:id/head_img")
    username_locator = ("xpath", '//*[@text="请输入账号"]')
    password_locator = ("id", "com.tpshop.malls:id/pwd_et")
    login_locator = ("id", "com.tpshop.malls:id/login_tv")
    home_page_locator = ("xpath",'//*[@text="首页"]')
    product_promotion_locator = ("xpath",'//*[@text="商品促销"]')
    good_locator = ("xpath",'//*[@text="【套餐赠耳机】HUAWEI/华为 畅享8 Plus 全面屏手机"]')
    now_buy_locator = ("xpath", '//*[@text="立即购买"]')
    sure_locator = ("xpath", '//*[@text="确定"]')
    use_balance_locator = ("id", "com.tpshop.malls:id/order_balance_sth")
    place_order_locator = ("xpath", '//*[@text="提交订单"]') # 提交订单
    balance_locator = ("id", "com.tpshop.malls:id/balance_tv") # 余额
    good_price_locator = ("id","com.tpshop.malls:id/balance_fee_tv") # 商品价格
    pay_password_locator = ("id","com.tpshop.malls:id/pwd_et") # 支付密码

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

    def get_balance(self,content):
        """获取余额"""
        return self.get_element_text(self.balance_locator,content)

    def get_good_price(self,content):
        """获取商品价格"""
        return self.get_element_text(self.good_price_locator,content)

    def click_home_page(self):
        """点击首页"""
        self.click(self.home_page_locator)

    def click_product_promotions(self):
        """点击促销产品"""
        self.click(self.product_promotion_locator)

    def click_good(self):
        """点击某个产品"""
        self.click(self.good_locator)

    def click_now_buy(self):
        """点击立即购买"""
        self.click(self.now_buy_locator)

    def click_sure(self):
        """点击确定"""
        self.click(self.sure_locator)

    def click_use_balance(self):
        """点击使用余额"""
        self.click(self.use_balance_locator)

    def click_place_order(self):
        """点击提交订单"""
        self.click(self.place_order_locator)

    def send_pay_password(self,password):
        """输入支付密码"""
        self.send_keys(self.password_locator,password)



if __name__ == '__main__':
    driver = open_mobile()
    sag = ShoppingActivityGoods(driver)
    # 点击我的
    sag.click_my()
    # sag.click_head()
    # sag.send_username("18428389548")
    # sag.send_password("123456")
    # sag.click_login()
    # 获取账户余额
    result = sag.get_balance("text")
    print(result)
    # 点击首页
    sag.click_home_page()
    # 点击促销商品
    sag.click_product_promotions()
    # 点击某个商品
    sag.click_good()
    # 点击立即购买
    sag.click_now_buy()
    # 点击确认
    sag.click_sure()
    # 使用账户余额购买
    sag.click_use_balance()
    # 获取商品的价格
    good_price = sag.get_good_price("text")
    # 去除商品价格前的￥符号
    price = good_price[1:]
    print(price)
    # 点击提交订单
    sag.click_place_order()
    # 输入支付密码
    sag.send_pay_password("123456")
    # 点击确定
    sag.click_sure()
    # 返回首页
    sag.page_back()
    sag.page_back()
    sag.page_back()
    # 点击我的
    sag.click_my()
    result1 = sag.get_balance("text")
    print(result1)
