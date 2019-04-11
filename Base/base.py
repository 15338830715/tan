from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Base:

    def __init__(self, driver):
        self.driver = driver

    # 定义一个方法叫 syy_find_element()
    def base_find_element(self, ele_feature, timeout=5, proll=1.0):
        """
        调用当前函数时可以返回一个具体的元素对象
        :param ele_feature: 是一个元组类型，代表对应元素的特征
        :return: object ，具体的元素对象
        """

        wait = WebDriverWait(self.driver, timeout, proll)
        return wait.until(lambda x: x.find_element(*ele_feature))

        # return WebDriverWait(self.driver, 5, 1).until(lambda x: x.find_element(*ele_feature))

    # 定义一个方法 完成多个元素的定位操作
    def base_find_elements(self, ele_feature):
        return self.driver.find_elements(*ele_feature)

    # 定义一个方法 完成单个元素点击的操作
    def base_click(self, feature):
        # 将来用户在调用syy_click() 方法的时候 只需要传入对应的元素特征
        # 依据特征找到元素 然后进行点击
        self.base_find_element(feature).click()

    # 定义一个方法 完成指定元素的点击操作
    def base_clicks(self, feature, num):
        """
        调用该函数时要求传入具体的元素特征和目标元素的编号
        :param feature:
        :return: None
        """
        self.base_find_elements(feature)[num].click()

    # 定义一个方法 完成指定输入框的内容写入
    def base_input(self, feature, value):
        self.base_find_element(feature).send_keys(value)

    # 定义一个方法用于获取当前设备的屏幕尺寸
    def base_get_windwow_size(self):
        """
        调用当前函数为自动返回设备的屏幕尺寸
        :return: 元组类型，包含设备的宽和高
        """
        w = self.driver.get_window_size()["width"]
        h = self.driver.get_window_size()["height"]
        return w,h

    # 定义一个方法用于实现滑屏
    def base_swipe(self, dir, duration=2000):

        # 因为使用 swipe 滑动必然会用到坐标，所以我们先动态获取设备的尺寸
        pos = self.base_get_windwow_size()

        # 依据调用者传入的方向来实现最终的滑动
        if dir == "l":
            self.driver.swipe(pos[0]*0.8, pos[1]*0.5, pos[0]*0.2, pos[1]*0.5, duration)
        elif dir == "r":
            self.driver.swipe(pos[0]*0.2, pos[1]*0.5, pos[0]*0.8, pos[1]*0.5, duration)
        elif dir == "t":
            self.driver.swipe(pos[0]*0.5, pos[1]*0.8, pos[0]*0.5, pos[1]*0.2, duration)
        elif dir == "b":
            self.driver.swipe(pos[0]*0.5, pos[1]*0.2, pos[0]*0.5, pos[1]*0.8, duration)

    # 定义一个函数 用于获取指定 toast 框的内容
    def base_get_toast_txt(self, msg):
        toast_feature = By.XPATH, "//*[contains(@text, '%s')]" % msg
        a = self.base_find_element(toast_feature, timeout=6, proll=0.1)
        return a.text

    # 定义工具方法：判断某个按钮是否为激活状态
    def base_is_enabled(self, feature):
        # 先找到目标元素
        ele_btn = self.base_find_element(feature)

        # 获取到当前元素的属性值
        attr_val = ele_btn.get_attribute("enabled")

        if attr_val == 'false':
            # 表示按钮不可点击 未激活
            return False
        else:
            return True

    # 定义工具函数：
    def base_assert_toast(self, msg):
        try:
            # 下面的代码如果有异常，用说明此时应当断言失败
            self.base_get_toast_txt(msg)

            # 如果我们能找到值，且这个值还等于预期，此时就通过
            if self.base_get_toast_txt(msg) == msg:
                return True
        except:
            return False

    # 定义工具函数：【 判断目标元素是否存在 】
    def base_element_exist_or_not(self, ele_feature):

        try:
            print(self.base_find_element(ele_feature).text)
            return True
        except:
            self.base_swipe("t", 4000)
            return self.base_element_exist_or_not(ele_feature)



