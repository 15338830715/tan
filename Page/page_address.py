import time

import allure
from selenium.webdriver.common.by import By

from Base.base import Base


class PageAddress(Base):

    # 提取当前界面中需要用到的元素特征
    address_manage_feature = By.ID, "com.yunmall.lc:id/setting_address_manage"
    address_new_featrue = By.ID, "com.yunmall.lc:id/address_add_new_btn"
    receipt_feature = By.ID, "com.yunmall.lc:id/address_receipt_name"
    phone_num_feature = By.ID, "com.yunmall.lc:id/address_add_phone"
    area_select_feature = By.ID, "com.yunmall.lc:id/address_province"
    detail_address_feature = By.ID, "com.yunmall.lc:id/address_detail_addr_info"
    save_btn_feature = By.ID, "com.yunmall.lc:id/button_send"
    address_list_feature = By.ID, "com.yunmall.lc:id/receipt_name"
    address_edit_feature = By.ID, "com.yunmall.lc:id/ymtitlebar_right_btn"
    address_del_feature = By.ID, "com.yunmall.lc:id/delete"
    address_confirm_feature = By.ID, "com.yunmall.lc:id/ymdialog_left_button"
    address_test_feature = By.ID, "com.yunmall.lc:id/rl_address"

    # 点击地址管理
    @allure.step(title="点击地址管理")
    def click_address_manage(self):
        self.base_click(self.address_manage_feature)

    # 点击 新增地址
    @allure.step(title="点击新增地址")
    def click_new_address(self):
        self.base_click(self.address_new_featrue)

    # 输入收件人
    @allure.step(title="输入收件人")
    def input_receipt(self, val):
        allure.attach("收件人描述", "收件人为%s" % val)
        self.base_input(self.receipt_feature, val)

    # 输入手机号
    @allure.step(title="输入手机号")
    def input_phone_num(self, val):
        allure.attach("手机号描述", "手机号为%s" % val)
        self.base_input(self.phone_num_feature, val)

    # 点击省市区按钮
    @allure.step(title="点击省市区下拉")
    def click_area_select(self):
        self.base_click(self.area_select_feature)
        time.sleep(1)

    # 选择省市区
    @allure.step(title="选择省市区")
    def select_area(self, province, city, area):

        allure.attach("省市区描述", "输入的值为%s， %s, %s" % (province, city, area))
        # 定义当前直辖市列表
        city_list = ["北京市", "天津市", "上海市", "重庆市"]

        # 利用方法被调用时传入的 省市区三个值 ，自动组装对应的元素特征
        province_feature = By.XPATH, "//*[@text='%s']" % province
        city_feature = By.XPATH, "//*[@text='%s']" % city
        area_feature = By.XPATH, "//*[@text='%s']" % area

        # 无论是否为直辖市都需要点击省份
        # 在点击省份之前需要先判断目标省份是否存在，如果存在则点击
        if self.base_element_exist_or_not(province_feature):
            self.base_click(province_feature)
            time.sleep(1)

        # 先区分当前是直辖市与否
        if province in city_list:
            self.driver.find_element(By.ID, "com.yunmall.lc:id/area_title").click()
            time.sleep(1)
        else:
            self.base_click(city_feature)
            time.sleep(1)

        # 无论是否为直辖市都需要点击区县
        if self.base_element_exist_or_not(area_feature):
            self.base_click(area_feature)

    # 输入详细地址
    @allure.step(title="输入详细地址")
    def input_detail_address(self, val):
        self.base_input(self.detail_address_feature, val)

    # 点击保存
    @allure.step(title="点击保存")
    def click_save(self):
        self.base_click(self.save_btn_feature)

    # 断言动作
    @allure.step(title="执行断言")
    def assert_address_add(self, receipt, phone_nume):
        # 无论断言成功与否我们都添加截图
        allure.attach("断言截图", self.driver.get_screenshot_as_png, allure.attach_type.PNG)
        btn_list = self.base_find_elements(self.address_list_feature)
        if len(btn_list) > 1:
            assert btn_list[1].text == "%s  %s" % (receipt, phone_nume)
        else:
            assert btn_list[0].text == "%s  %s" % (receipt, phone_nume)

    # 点击编辑
    def click_address_edit(self):
        self.base_click(self.address_edit_feature)

    # 点击删除
    def click_address_del(self):
        self.base_click(self.address_del_feature)

    # 点击确定
    def click_address_confirm(self):
        self.base_click(self.address_confirm_feature)

    # 定义获取当前地址条数的动作
    def get_address_count(self):
        del_list = self.base_find_elements(self.address_test_feature)
        # 获取到地址的条数之后，我们需要进行判断
        # 如果当前条数为0 则：让当前程序停止
        # 如果不为0 则正常删除，所以我们返回当前的条数
        if len(del_list) == 0:
            return 0
        else:
            return len(del_list)

