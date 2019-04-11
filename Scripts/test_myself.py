import time
import pytest
from Base.get_data import get_data
from Page.page import Page

class TestMyself:

    def setup(self):
        self.action =Page().init_page_myself
    def teardown(self):
        self.action.driver.quit()

    # @pytest.mark.skip()
    @pytest.mark.parametrize("obj", get_data("myself", "login_no_num"))
    def test_login_no_num(self, obj):
        Page().init_page_home.into_page()
        # 在这里为了避免被操作的元素还未出现，可以设置强制等待，让主界面内容进行加载渲染
        time.sleep(2)

        # 点击 我
        self.action.click_myself()

        # 点击使用已有账号登录
        self.action.click_exist_num()

        # 输入账号
        self.action.input_num(obj[0])

        # 输入密码
        self.action.input_pwd(obj[1])

        # 点击登录
        self.action.click_login()

        # 断言账号不存在用例执行是否通过
        self.action.assert_toast("此用户不存在")





