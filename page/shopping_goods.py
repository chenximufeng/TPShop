from common.base import Base
from common.base import open_mobile

class ShoppingGoods(Base):
    my_locator = ("xpath", '//*[@text="我的"]')
    head_locator = ("id", "com.tpshop.malls:id/head_img")
    username_locator = ("xpath", '//*[@text="请输入账号"]')
    password_locator = ("id", "com.tpshop.malls:id/pwd_et")
    login_locator = ("id", "com.tpshop.malls:id/login_tv")
    home_page_locator = ("xpath", '//*[@text="首页"]')
    classification_locator = ("xpath", '//*[@text="分类"]')
    clothes_locator = ("xpath", '//*[@text="服饰"]')
    new_goods_locator = ("xpath", '//*[@text="新品推荐"]')
    good_locator = ("id","com.tpshop.malls:id/product_pic_img")
    now_buy_locator = ("xpath", '//*[@text="立即购买"]')
    sure_locator = ("xpath", '//*[@text="确定"]')
    use_balance_locator = ("id", "com.tpshop.malls:id/order_balance_sth")
    place_order_locator = ("xpath", '//*[@text="提交订单"]')
    balance_locator = ("id", "com.tpshop.malls:id/balance_tv")  # 余额
    good_price_locator = ("id", "com.tpshop.malls:id/balance_fee_tv")  # 商品价格
    pay_password_locator = ("id", "com.tpshop.malls:id/pwd_et")  # 支付密码

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

    def click_classification(self):
        """点击分类"""
        self.click(self.classification_locator)

    def click_clothes(self):
        """点击服饰"""
        self.click(self.clothes_locator)

    def click_new_goods(self):
        """点击新新品推荐"""
        self.click(self.new_goods_locator)

    def click_good(self):
        """点击商品"""
        self.click_all_element(self.good_locator,1)

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
    sg = ShoppingGoods(driver)
    sg.click_my()
    # sg.click_head()
    # sg.send_username("18428389548")
    # sg.send_password("123456")
    # sg.click_login()
    result = sg.get_balance("text")
    start_balance = float(result)
    print(start_balance)
    sg.click_home_page()
    sg.click_classification()
    sg.click_clothes()
    sg.click_new_goods()
    sg.click_good()
    sg.click_now_buy()
    sg.click_sure()
    sg.click_use_balance()
    good_price = sg.get_good_price("text")
    price = good_price[1:]
    price1 = float(price)
    print(price1)
    sg.click_place_order()
    sg.send_pay_password("123456")
    sg.click_sure()
    sg.page_back()
    sg.page_back()
    sg.page_back()
    sg.click_my()
    result1 = sg.get_balance("text")
    end_balance = float(result1)
    print(end_balance)