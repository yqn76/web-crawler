from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import json

def crawl_books(keywords,pages):
    driver = webdriver.Chrome(service=Service(r"D:\chrome浏览器\chromedriver.exe"))
    driver.maximize_window()
    driver.get(url=r"https://www.jd.com/")
    search=driver.find_element(By.ID,'key')
    enter=driver.find_element(By.CLASS_NAME,'button')
    search.send_keys(keywords)
    enter.click()
    time.sleep(1)
    for page in range(pages):
        scroll_height=int(driver.execute_script("return document.body.scrollHeight"))
        for i in range(1, scroll_height,20):
            driver.execute_script("window.scrollTo(840,{})".format(i))
            time.sleep(0.01)
        photos = driver.find_elements(By.CLASS_NAME, "gl-item")
        titles = driver.find_elements(By.CLASS_NAME, "p-name")
        prices = driver.find_elements(By.CLASS_NAME, "p-price")
        stops = driver.find_elements(By.CSS_SELECTOR, ".curr-shop.hd-shopname")
        locals = driver.find_elements(By.CLASS_NAME, "p-img a")
        for num in range(0, len(photos)):
            file={"商标":titles[num].text,"价格":prices[num].text,"店铺":stops[num].text,"商品的URL":locals[num].get_attribute("href")}
            with open("666.txt", "a+",encoding="utf-8") as f:
                f.writelines(file)

        next_page = driver.find_element(By.PARTIAL_LINK_TEXT, "下一页")
        next_page.click()
        time.sleep(0.1)
    driver.close()

if __name__=='__main__':
    pages=1
    keywords='网易春风'
    crawl_books(keywords,pages)
