from selenium import webdriver
from lxml import etree
import re
def get_url (url):
    browser = webdriver.Chrome()
    browser.get(url)
    html=browser.page_source
    browser.quit()
    return str(html)
def main (num):
    html=get_url('https://www.heavens-above.com/SatInfo.aspx?satid={}&'.format(num))
    html=etree.HTML(html)
    title=html.xpath('//title/text()')
    r=re.compile('(\S+) - 人造卫星信息')
    title=r.findall(title[0])
    title=title[0]
    infor=html.xpath('//div[@style="width:750px"]//text()')
    infor='\n'.join(infor)
    r=re.compile(r'([^\n\t]+)')
    infor=r.findall(infor)
