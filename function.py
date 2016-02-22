__author__ = 'xiaolin'
#coding=utf-8
import urllib

def gethtml(url):
    page=urllib.urlopen(url)
    html=page.read()
    return html

html= gethtml("http://so.baike.com/s/tupian/%E4%B8%AD%E5%9B%BD%E9%82%AE%E7%94%B5%E5%A4%A7%E5%AD%A6&prd=button_tupian_search")

print html
