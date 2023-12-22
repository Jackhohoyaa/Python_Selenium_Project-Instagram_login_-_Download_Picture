from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import requests as rq
import os
import time
import re
starttime=time.time()

Options().chrome_executabel_path="C:\Program Files\Google\Chrome\Application\chrome.exe"
driver=webdriver.Chrome(Options())  
def connect(url):
    driver.get(url)
    driver.maximize_window()#將視窗最大化
    time.sleep(1)
def log_in(account,password):
    account_name=driver.find_element(By.CSS_SELECTOR,"[name=username]")
    account_name.send_keys(account)
    password_name=driver.find_element(By.CSS_SELECTOR,"[name=password]")
    password_name.send_keys(password)
    submit=driver.find_element(By.CSS_SELECTOR,"[type=submit]")
    submit.send_keys(Keys.ENTER)
    time.sleep(5)
def click():
    driver.find_element(By.CLASS_NAME,"x9f619.x3nfvp2.xr9ek0c.xjpr12u.xo237n4.x6pnmvc.x7nr27j.x12dmmrz.xz9dl7a.xn6708d.xsag5q8.x1ye3gou.x80pfx3.x159b3zp.x1dn74xm.xif99yt.x172qv1o.x10djquj.x1lhsz42.xzauu7c.xdoji71.x1dejxi8.x9k3k5o.xs3sg5q.x11hdxyr.x12ldp4w.x1wj20lx.x1lq5wgf.xgqcy7u.x30kzoy.x9jhf4c").click()
    time.sleep(3)
    click=driver.find_element(By.CLASS_NAME,"_a9--._ap36._a9_0").click()
    time.sleep(3)
def search(name):
    links=[]
    search=driver.get("https://www.instagram.com/%s/"%(name))
    time.sleep(5)
    for _ in range(2): 
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(2)
    rawlink=driver.find_elements(By.TAG_NAME,"a")
    time.sleep(3)
    for i in rawlink:
        link=i.get_attribute("href")
        if re.search("https://www.instagram.com/p/.*",link):
                links.append(link)            
    return links    
def pics_link():
    pic_link_list=[]
    for j in range(len(links)):
        driver.get(links[j])
        time.sleep(3)
        pic_link=driver.find_element(By.CLASS_NAME,"x5yr21d.xu96u03.x10l6tqk.x13vifvy.x87ps6o.xh8yej3")
        pic_link=pic_link.get_attribute("src")
        pic_link_list.append(pic_link)
    driver.minimize_window()
    return pic_link_list
def create_dir(dirname):
    if not os.path.exists(dirname):
        os.mkdir(dirname)
def write_in():
    print("開始下載圖片")
    for i in range(len(pic_link_list)):
        with open(name + '/' + '%s'%(links[i][-12:-1]) + '.jpg','ab') as file:
            file.write(rq.get(pic_link_list[i]).content)
        print("下載第%d張"%(i+1))    
        time.sleep(1)    
    print("下載完成!!")              
    
if __name__ == "__main__":
    instagram_login='https://www.instagram.com/'
    account=input("請輸入帳號:")
    password=input("請輸入密碼:")
    name=input("請輸入欲下載圖片之帳號名稱:")
    connect(instagram_login)
    log_in(account,password)
    click()
    links=search(name)
    pic_link_list=pics_link()
    create_dir(name)
    write_in()
    endtime=time.time()   
    time=endtime-starttime
    print("總共耗時:%d分%.2f秒"%(time//60,time%60))    


