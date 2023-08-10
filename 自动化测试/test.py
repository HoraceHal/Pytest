# 导入webdriver
from appium import webdriver
# 初始化参数
desired_caps = {
 'platformName': 'Android', # 被测手机是安卓
 'platformVersion': '13', # 手机安卓版本
 'deviceName': 'mic', # 设备名，安卓手机可以随意填写
 'appPackage': 'com.ft.account', # 启动APP Package名称
 'appActivity': '.MainActivity', # 启动Activity名称
 'unicodeKeyboard': True, # 使用自带输入法，输入中文时填True
 'resetKeyboard': True, # 执行完程序恢复原来输入法
 'noReset': True, # 不要重置App，如果为False的话，执行完脚本后，app的数据会清空，比如
 'newCommandTimeout': 6000,
 'automationName': 'UiAutomator2'
}
# 连接Appium Server，初始化自动化环境
driver = webdriver.Remote('http://localhost:4723')
# 退出程序，记得之前没敲这段报了一个错误 Error: socket hang up 啥啥啥的忘记了，有兴趣可以t
driver.quit()
