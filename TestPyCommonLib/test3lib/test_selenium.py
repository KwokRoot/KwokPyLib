import time

from selenium import webdriver

# chromedriver下载地址：
# http://chromedriver.storage.googleapis.com/index.html
# http://npm.taobao.org/mirrors/chromedriver/
# browser = webdriver.Chrome(executable_path=r"\Kwok\Work\Other\chromedriver.exe")

browser = webdriver.Firefox(executable_path=r"\Kwok\Work\Other\geckodriver.exe")

browser.maximize_window()

browser.get("https://detail.vip.com/detail-1710615435-6919569576558531403.html")
browser.implicitly_wait(10)

# print(browser.find_element_by_name('email'))
# print(browser.find_element_by_name('passworld').text)
# browser.find_element_by_id("dologin").click

# browser.find_element_by_id("kw").send_keys("HelloWorld")
# browser.find_element_by_id("su").click()

# print(browser.find_element_by_id("normalLoginTab").find_elements_by_tag_name("input"))

elements = browser.find_elements_by_xpath("/html/body/div[4]/div[1]/div[3]/div[3]/div[1]/div[4]/div[2]/div/div[1]/div/span[1]")
print(elements[0].text)

time.sleep(2)
browser.quit()

