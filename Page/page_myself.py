from time import sleep

import allure
from selenium.webdriver.common.by import By

from Base.base import Base


class PageMyself(Base):

    # 将当前界面中需要用到的元素信息抽离出来
    myself_btn_feature = By.ID, "com.yunmall.lc:id/tab_me"
    exist_num_feature = By.ID, "com.yunmall.lc:id/gotologon"
    num_input_feature = By.ID, "com.yunmall.lc:id/logon_account_textview"
    pwd_input_feature = By.ID, "com.yunmall.lc:id/logon_password_textview"
    login_btn_feature = By.ID, "com.yunmall.lc:id/logon_button"
    nick_name_feature = By.ID, "com.yunmall.lc:id/tv_user_nikename"
    setting_btn_feature = By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_layout"
    quit_btn_feature = By.ID, "com.yunmall.lc:id/setting_logout"
    confirm_btn_feature = By.ID, "com.yunmall.lc:id/ymdialog_right_button"
    login_feature = By.ID, "com.yunmall.lc:id/logon_button"

    # 点击 我
    @allure.step(title="执行点我")
    def click_myself(self):
        self.base_click(self.myself_btn_feature)

    # 点击使用已有账号登录
    @allure.step(title="点击使用已有账号")
    def click_exist_num(self):
        self.base_click(self.exist_num_feature)

    # 输入账号
    @allure.step(title="输入账号")
    def input_num(self, num_val):
        allure.attach("账号描述", "此时输入的账号为%s" % num_val, allure.attach_type.TEXT)
        self.base_input(self.num_input_feature, num_val)

    # 输入密码
    @allure.step(title="输入密码")
    def input_pwd(self, pwd_val):
        allure.attach("账号描述", "此时输入的账号为%s" % pwd_val, allure.attach_type.TEXT)
        self.base_input(self.pwd_input_feature, pwd_val)

    # 点击登录
    @allure.step(title="点击登录")
    def click_login(self):
        self.base_click(self.login_btn_feature)

    # 定义一个断言 toast 框的动作
    @allure.step(title="执行断言")
    def assert_toast(self, toast_msg):
        allure.attach("断言截图", self.driver.get_screenshot_as_png(), allure.attach_type.PNG)
        assert self.base_assert_toast(toast_msg)

    def is_login(self):
        try:
            self.base_find_element(self.nick_name_feature)
            print(self.base_find_element(self.nick_name_feature).text)
            return True
        except:
            return False

    # 点击设置
    @allure.step(title="点击设置")
    def click_setting(self):
        self.base_click(self.setting_btn_feature)

    # 点击退出
    def click_quit(self):
        self.base_click(self.quit_btn_feature)

    # 点击确认
    def click_confirm(self):
        self.base_click(self.confirm_btn_feature)

    # 定义断言是否可登录动作
    def assert_if_login(self):

        return not self.base_is_enabled(self.login_feature)

        # a = self.syy_is_enabled(self.login_feature)
        #
        # if a == True:
        #     print("当前是激活的状态")
        #     return False
        # else:
        #     print("当前是未激活的")
        #     return True




