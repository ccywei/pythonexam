# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 10:15:27 2019
@author: ccywei
"""

import re 
import requests  
from pyquery import PyQuery as pq

def getHtml(url, code="utf-8"):  
    try:  
        r =requests.get(url)  
        r.raise_for_status()  
        r.encoding = code  
# =============================================================================
#         print("test")  
# =============================================================================
        return r.text  
    except:  
        return ""   
    
    
def main():  
    print("start")
    baidunameurl='http://www.baidu.com/s?wd=崔亚伟'  
    doc= pq(getHtml(baidunameurl))
    mlist = doc('#content_left h3.t a').items()
    i=0
    for li in mlist :
        i=i+1
        print('标题：'+li.text())
        print('链接：'+li.attr('href'))
    print(i)
    print("end")  
  
  
main()  
