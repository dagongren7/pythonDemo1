from time import sleep
from  appium import webdriver

desired_caps={
  "platformName": "Android",
  "platformVersion": "4.4.2",
  "deviceName": "127.0.0.1:62001",
  "appPackage": "com.tal.kaoyan",
  "appActivity": "com.tal.kaoyan.ui.activity.HomeTabActivity",
  "noReset": "true"
}

driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)


#获取屏幕尺寸
def get_size():
    x=driver.get_window_size()['width']
    y=driver.get_window_size()['height']
    return x,y

#显示屏幕尺寸（width,height）
l=get_size()
print(l)

#向左滑动
def swipeLeft():
    l=get_size()
    x1=int(l[0]*0.9)
    y1=int(l[1]*0.5)
    x2=int(l[0]*0.1)
    driver.swipe(x1,y1,x2,y1,1000)

def swipeUp():
    l = get_size()
    x1 = int(l[0] * 0.5)
    y1 = int(l[1] * 0.95)
    y2 = int(l[1] * 0.35)
    driver.swipe(x1, y1, x1, y2, 1000)

def swipeDown():
    l=get_size()
    x1 = int(l[0] * 0.5)
    y1 = int(l[1] * 0.35)
    y2 = int(l[1] * 0.85)
    driver.swipe(x1, y1, x1, y2, 1000)

def swipeRight():
    l=get_size()
    y1 = int(l[1] * 0.5)
    x1 = int(l[0] * 0.25)
    x2 = int(l[0] * 0.95)
    driver.swipe(x1, y1, x2, y1, 1000)

driver.implicitly_wait(5)

def drag_and_drop():
    s1 = driver.find_element_by_xpath("//*[@text='周二']")
    print(s1)
    s2 = driver.find_element_by_xpath("//*[@instance='11']")
    print(s2)
    driver.drag_and_drop(s2,s1)
#向左滑动2次
# for i in range(2):
#     swipeUp()
#     sleep(1)

drag_and_drop()
sleep(3)

driver.close()