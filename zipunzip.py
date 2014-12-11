# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 17:01:16 2014

@author: zhaoyd
"""

#coding=utf-8
#甄码农python代码
#使用zipfile做目录压缩，解压缩功能
 
import os,os.path
import zipfile
 
def zip_dir(dirname,zipfilename):
    filelist = []
    if os.path.isfile(dirname):
        filelist.append(dirname)
    else :
        for root, dirs, files in os.walk(dirname):
            for name in files:
                filelist.append(os.path.join(root, name))
         
    zf = zipfile.ZipFile(zipfilename, "w", zipfile.zlib.DEFLATED)
    for tar in filelist:
        arcname = tar[len(dirname):]
        #print arcname
        zf.write(tar,arcname)
    zf.close()
 
 
def unzip_file(zipfilename, unziptodir,needdir='all'):
    if not os.path.exists(unziptodir): os.mkdir(unziptodir, 0777)
    zfobj = zipfile.ZipFile(zipfilename)
    for name in zfobj.namelist():
        name = name.replace('\\','/')
        namedis=name.split('/')
        if needdir!='all':           
            if namedis[1]!=needdir:
                continue
        name2=''
        for ith in range(len(namedis)-2):
            ith=ith+1
            name2+=namedis[ith]+'/'
        if namedis[-1]!='':
            name2+=namedis[-1]                   
        
        if name2.endswith('/'):
            os.mkdir(os.path.join(unziptodir, name2))
        else:            
            ext_filename = os.path.join(unziptodir, name2)
            ext_dir= os.path.dirname(ext_filename)
            if not os.path.exists(ext_dir) : os.mkdir(ext_dir,0777)
            outfile = open(ext_filename, 'wb')
            outfile.write(zfobj.read(name))
            outfile.close()
 
if __name__ == '__main__':
    zip_dir(r'goagent-goagent-v3.1.25-6-g6ddcddc.zip',r'goagent-goagent-v3.1.25-6-g6ddcddc.zip.zip')
    unzip_file(r'goagent-goagent-v3.1.25-6-g6ddcddc.zip',r'goagent','local')
