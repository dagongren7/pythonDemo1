from  appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

desired_caps={}
desired_caps['platformName']='Android'
desired_caps['platformVersion']='4.4.2'
desired_caps['deviceName']='127.0.0.1:62001'

desired_caps['app']=r'F:\04.App自动化appium(python语言版)\appium教程相关软件\第四章软件\App\dr.fone3.2.0.apk'
desired_caps['appPackage']='com.wondershare.drfone'
desired_caps['appActivity']='com.wondershare.drfone.ui.activity.WelcomeActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(5)

print('click BackupBtn')
driver.find_element_by_id('com.wondershare.drfone:id/btnBackup').click()

WebDriverWait(driver,8).until(lambda x:x.find_element_by_id('com.wondershare.drfone:id/btnRecoverData'))
print('click NextBtn')
driver.find_element_by_id('com.wondershare.drfone:id/btnRecoverData').click()

WebDriverWait(driver,8).until(lambda x:x.find_element_by_class_name('android.webkit.WebView'))
contexts=driver.contexts
print(contexts)


#需android4.4及以上版本的系统中才会输出更多的webview
print('switch conetext')
driver.switch_to.context('WEBVIEW_com.wondershare.drfone')
print('edit email')
driver.find_element_by_id('email').send_keys('shuqing@wondershare.cn')
print('click sendBtn')
driver.find_element_by_class_name('btn_send').click()

#切换context 点击返回
driver.switch_to.context('NATIVE_APP')
driver.find_element_by_class_name('android.widget.ImageButton').click()