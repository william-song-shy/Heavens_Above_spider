from selenium import webdriver
from bs4 import BeautifulSoup
import re
def get_url (url):
    browser = webdriver.Chrome()
    browser.get(url)
    html=browser.page_source
    browser.quit()
    return str(html)

num=input ()
html=get_url('https://www.heavens-above.com/SatInfo.aspx?satid={}&'.format(num))
s=BeautifulSoup(html,'html.parser')
r=re.compile('(\S*) - 人造卫星信息')
title=r.findall(s.title.string)
title=title[0]
