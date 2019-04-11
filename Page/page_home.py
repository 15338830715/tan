import time

from selenium.webdriver.common.by import By

from Base.base import Base


class PageHome(Base):

    # 将当前界面需要用到的元素信息提取出来
    skip_btn_feature =  By.ID, "com.yunmall.lc:id/view_mask"
    tab_home_feature = By.ID, "com.yunmall.lc:id/tab_home"

    def into_page(self):

        # 强制等待
        time.sleep(3)

        try:
            self.base_find_element(self.tab_home_feature)
            print("欢迎使用")
        except:
            # 点击跳过
            self.base_click(self.skip_btn_feature)




