from appium import webdriver


def driver():
    desired_caps = dict()
    desired_caps["platformName"] = "android"
    desired_caps["platformVersion"] = "5.1"
    desired_caps["deviceName"] = "***"
    desired_caps["noReset"] = True
    desired_caps["unicodeKeyboard"] = True
    desired_caps["resetKeyboard"] = True
    desired_caps['automationName'] = 'Uiautomator2'
    desired_caps["appPackage"] = "com.yunmall.lc"
    desired_caps["appActivity"] = "com.yunmall.ymctoc.ui.activity.LaunchActivity"

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

    # 为了将来调用函数时可以在外部使用到 driver 需要 return
    return driver



