# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 17:07:24 2014

@author: zhaoyd
"""

import urllib2 

def download_file(url,filename):
    f = urllib2.urlopen(url) 
    with open(filename, "wb") as code:
        code.write(f.read()) 
    return 0

if __name__ == '__main__':
    url='https://codeload.github.com/goagent/goagent/legacy.zip/3.0'
    f = urllib2.urlopen(url) 
    print f.headers.dict['content-disposition']
    