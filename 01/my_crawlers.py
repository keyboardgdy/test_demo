from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
# import numpy as np
# import pandas as pd
import csv

driver = webdriver.Chrome()  # Chrome浏览器
time.sleep(5)
url = "https://iftp.chinamoney.com.cn/english/bdInfo/"
# 打开网页
driver.get(url)  # 打开url网页 比如 driver.get("http://www.baidu.com")

ele1 = driver.find_element(By.ID, "Bond_Type_select")
select_ele = Select(ele1)
# 通过下拉元素的文本内容选择下拉元素
select_ele.select_by_visible_text("Treasury Bond")
time.sleep(2)

ele2 = driver.find_element(By.ID, "Issue_Year_select")
select_ele = Select(ele2)
# 通过下拉元素的文本内容选择下拉元素
select_ele.select_by_visible_text("2023")
time.sleep(3)

search_button = driver.find_element(By.XPATH, '//*[@id="resetValue"]/div/div[8]/a[1]')
search_button.click()
time.sleep(2)

with open("body_text.txt", "a", encoding='gbk') as file:
    file.write("ISIN ,Bond Code ,Issuer ,Bond Type ,Issue Date ,Latest Rating")


def txt_to_csv01(mode):
    csvFile = open("result.csv", 'a+', newline='', encoding='utf-8')
    csvFile.truncate(0)
    writer = csv.writer(csvFile)
    csvRow = []

    f = open("body_text.txt", 'r+', encoding='GBK')
    for line in f:
        csvRow = line.split(mode)
        print(csvRow)
        writer.writerow(csvRow)
    f.truncate(0)

    f.close()
    csvFile.close()


txt_to_csv01(mode=",")

pages_div = driver.find_element(By.XPATH, '//*[@id="pagi-bond-market"]/li[1]/span/span')
pages_number = int(pages_div.text)
print(pages_number)

for _ in range(0, pages_number):
    body_tr = driver.find_element(By.XPATH, '//*[@id="sheet-bond-market"]/div[1]/div/table/tbody')
    # print(body_tr.text)
    body_text = body_tr.text

    with open("body_text.txt", "a", encoding='gbk') as file:
        file.write(body_text + "\n")

    next_button = driver.find_element(By.XPATH, '//*[@id="pagi-bond-market"]/li[4]/a')
    next_button.click()
    time.sleep(1)


def txt_to_csv02(mode):
    csvFile = open("result.csv", 'a+', newline='', encoding='utf-8')
    writer = csv.writer(csvFile)
    csvRow = []

    f = open("body_text.txt", 'r+', encoding='GBK')
    for line in f:
        csvRow = line.split(mode)
        # print(csvRow)
        seq1 = (csvRow[2:11])
        seq2 = (csvRow[11:13])
        manage_csv = [csvRow[0], csvRow[1], " ".join(seq1), " ".join(seq2), csvRow[13], csvRow[14].replace('\n', '')]
        print(manage_csv)
        writer.writerow(manage_csv)
    f.truncate(0)

    f.close()
    csvFile.close()


txt_to_csv02(mode=" ")
