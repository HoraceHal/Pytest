# test_sample.py
import unittest
from time import sleep
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestBBS(unittest.TestCase):

    def setUp(self):
        desired_caps = {
            'deviceName': 'JEF_AN20',
            'automationName': 'UiAutomator2',
            'platformName': 'Android',
            'platformVersion': '13',
            'appPackage': 'com.ft.account',
            'appActivity': '.MainActivity',
            'noReset': True,
        }

        self.dr = webdriver.Remote(
            command_executor='http://127.0.0.1:4723',
            desired_capabilities=desired_caps)

    def tearDown(self):
        self.dr.quit()

    def test_bbs(self):
        # 定义运行环境
        sleep(5)
        self.dr.find_element(MobileBy.ID, "com.meizu.flyme.flymebbs:id/nw").click()
        sleep(2)
        self.dr.find_element(MobileBy.ID, "com.meizu.flyme.flymebbs:id/nw").send_keys("flyme")
        self.dr.find_element(MobileBy.ID, "com.meizu.flyme.flymebbs:id/o1").click()
        sleep(2)

        title_list = self.dr.find_elements(MobileBy.ID, "com.meizu.flyme.flymebbs:id/a29")
        for title in title_list:
            print(title.text)
            self.assertIn("lyme", title.text)


if __name__ == '__main__':
    unittest.main()
