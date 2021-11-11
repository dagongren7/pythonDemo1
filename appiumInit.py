import time

from appium import webdriver

desired_caps = {
  "platformName": "Android",
  "platformVersion": "9",
  "deviceName": "SHUGUO S3",
  "appPackage": "org.codeaurora.gallery",
  "appActivity": "com.android.gallery3d.app.GalleryActivity",
  "unicodeKeyboard": "true",
  "resetKeyboard": "true",
  "noReset": "true"
}


# 声明手机驱动对象
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
driver.implicitly_wait(5)
# desired_caps['appActivity'] = 'com.android.shuguotalk.activity.MainActivity'



# 退出手机驱动对象
driver.quit()