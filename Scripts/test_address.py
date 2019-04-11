import time

import pytest

from Base.get_data import get_data
from Page.page import Page


class TestAddress:

    def setup(self):
        self.action = Page().init_page_address

    # @pytest.mark.skip()
    @pytest.mark.parametrize("obj", get_data("address", "address_new"))
    def test_address_new(self, obj):
        # 进入主界面,通掉用page_home里的页面动作
        Page().init_page_home.into_page()


        # 点击我，通过掉用page_myself里的页面动作
        self.use_myself=Page().init_page_myself
        self.use_myself.click_myself()

        # 判断用户是否登录 通过掉用page_myself里的页面动作
        if not self.use_myself.is_login():
            self.use_myself.click_exist_num()
            self.use_myself.input_num(18610453007)
            self.use_myself.input_pwd(123456)
            self.use_myself.click_login()

        # 点击设置 通过掉用page_myself里的页面动作
        self.use_myself.click_setting()


        # 点击地址管理
        self.action.click_address_manage()

        # 点击 新增地址
        self.action.click_new_address()

        # 输入收件人
        self.action.input_receipt(obj[0])

        # 输入手机号
        self.action.input_phone_num(obj[1])

        # 展开省市区下拉
        self.action.click_area_select()

        # 选择省市区
        self.action.select_area(obj[2], obj[3], obj[4])

        # 输入详细地址
        self.action.input_detail_address(obj[5])

        # 点击保存
        self.action.click_save()
        time.sleep(2)

        # 断言
        self.action.assert_address_add(obj[0], obj[1])

    @pytest.mark.skip()
    def test_address_del(self):
        # 进入主界面
        Page().init_page_home.into_page()

        # 点击我
        Page().init_page_myself.click_myself()

        # 判断用户是否登录
        if not Page().init_page_myself.is_login():
            Page().init_page_myself.click_exist_num()
            Page().init_page_myself.input_num(18610453007)
            Page().init_page_myself.input_pwd(123456)
            Page().init_page_myself.click_login()

        # 点击设置
        self.action.click_setting()

        # 点击地址管理
        self.action.click_address_manage()
        time.sleep(1)

        # 获取删除前的地址条数
        before_del = self.action.get_address_count()

        if not before_del:
            return
        else:
            # 点击编辑
            self.action.click_address_edit()

            # 点击删除
            self.action.click_address_del()

            # 点击确定
            self.action.click_address_confirm()
            time.sleep(1)

        # 获取删除后的地址条数
        after_del = self.action.get_address_count()

        # 断言
        assert before_del-after_del == 1

    @pytest.mark.skip()
    def test_address_del_all(self):
        # 进入主界面
        Page().init_page_home.into_page()

        # 点击我
        Page().init_page_myself.click_myself()

        # 判断用户是否登录
        if not Page().init_page_myself.is_login():
            Page().init_page_myself.click_exist_num()
            Page().init_page_myself.input_num(18610453007)
            Page().init_page_myself.input_pwd(123456)
            Page().init_page_myself.click_login()

        # 点击设置
        self.action.click_setting()

        # 点击地址管理
        self.action.click_address_manage()
        time.sleep(1)

        # 获取删除前的地址条数
        before_del = self.action.get_address_count()
        print(before_del)

        # 执行删除
        for i in range(before_del):
            # 点击编辑
            self.action.click_address_edit()
            # 点击删除
            self.action.click_address_del()
            # 点击确认
            self.action.click_address_confirm()
            time.sleep(1)

        # 获取删除后的地址条数
        after_del = self.action.get_address_count()
        print(after_del)

        # 断言
        assert after_del == 0




