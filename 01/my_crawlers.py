from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  # Chrome浏览器
time.sleep(5)
url = "https://iftp.chinamoney.com.cn/english/bdInfo/"
# 打开网页
driver.get(url)  # 打开url网页 比如 driver.get("http://www.baidu.com")

ele1 = driver.find_element(By.ID, "Bond_Type_select")
select_ele = Select(ele1)
# 通过下拉元素的文本内容选择下拉元素
select_ele.select_by_visible_text("Treasury Bond")
time.sleep(1)

ele2 = driver.find_element(By.ID, "Issue_Year_select")
select_ele = Select(ele2)
# 通过下拉元素的文本内容选择下拉元素
select_ele.select_by_visible_text("2023")
time.sleep(1)

search_button = driver.find_element(By.XPATH, '//*[@id="resetValue"]/div/div[8]/a[1]')
search_button.click()
time.sleep(1)

time.sleep(1)






