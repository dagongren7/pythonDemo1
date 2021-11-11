import time

import pytesseract
import requests
from PIL import Image
from selenium import webdriver
from lxml import etree

driver = webdriver.Chrome()

url = 'http://sgs2.pocyun.com:48000/SG_sns/admin/login'
driver.get(url)

driver.implicitly_wait(5)

el1 = driver.find_element_by_xpath('//*[@id="login_name"]')
el1.send_keys('admin')

el2 = driver.find_element_by_xpath('//*[@id="login_pwd"]')
el2.send_keys('123456')
driver.implicitly_wait(3)

# 获取验证码
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
    }
page_text = requests.get(url=url, headers=headers).text
tree = etree.HTML(page_text)
cod_img_src = tree.xpath('//*[@id="verifyimg"]/@src')[0]
print("cod_img_src"+cod_img_src)
cod_data = requests.get(url=cod_img_src,headers=headers).content
with open('./code.jpg', 'wb') as fp:
    fp.write(cod_data)
text = pytesseract.image_to_string(Image.open(r'./code.jpg'))
print("验证码："+text)
driver.implicitly_wait(3)

el3 = driver.find_element_by_xpath('//*[@id="login_verify"]')
el3.send_keys(text)
driver.implicitly_wait(3)

el4 = driver.find_element_by_xpath('//*[@id="reg"]/ul/li[4]/span')
el4.click()

time.sleep(3)
driver.close()