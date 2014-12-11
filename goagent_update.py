# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 18:57:55 2014

@author: zhaoyd
"""

import zipunzip
import update_file
import urllib2
import glob


url='https://codeload.github.com/goagent/goagent/legacy.zip/3.0'
f = urllib2.urlopen(url) 
outname=f.headers.dict['content-disposition'].split('=')[1]
if glob.glob('.\\'+outname)==[]:
    with open(outname, "wb") as code:
        code.write(f.read())
    print 'backup proxy.ini ..........................\n' 
    update_file.moveFileto(r'../local/proxy.ini',r'proxybak')     
    print 'unzip downloaded file ..........................\n'     
    zipunzip.unzip_file(outname,r'latest','local')
    print 'updating file ..........................\n'         
    update_file.copyFiles(r'./latest/local',r'../local')
    print 'recovery proxy.ini ......................\n' 
    update_file.moveFileto(r'proxybak',r'./local/proxy.ini')
    print 'chmod for specific files'
    os.system('./change_mod.sh')  
else:
    print 'goagent is the latest version'
