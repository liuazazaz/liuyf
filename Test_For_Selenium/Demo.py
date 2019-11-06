from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
# 定义一个chrome浏览器驱动。
path = r"D:\Python37\chromedriver.exe"
url = "https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc"
browser = webdriver.Chrome(path)

time.sleep(1)
browser.get(url)
# webdriver = webdriver.Chrome()
# webdriver.get('https://www.12306.cn/index/')
time.sleep(1)
from_city = browser.find_element_by_id("fromStationText")
to_city = browser.find_element_by_id("toStationText")

from_city.click()
from_city.clear()
from_city.send_keys("北京\n")

to_city.click()
to_city.clear()
to_city.send_keys('上海\n')
# browser.find_element_by_id('search_one').click()

choice_time = Select(browser.find_element_by_id("cc_start_time"))
choice_time.select_by_visible_text('12:00--18:00')

data = browser.find_element_by_css_selector("#date_range li:nth-child(5)")
data.click()
# browser.find_element_by_id('query_ticket').click()
time.sleep(3)
xpath = '//tbody[@id="queryLeftTable"]//td[2][@class]/../td[1]//a'
train_list = browser.find_element_by_xpath(xpath)

for train in train_list:
    print(train.text)

browser.quit()
# webdriver.find_element_by_id('su').click()