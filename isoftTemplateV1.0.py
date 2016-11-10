#!/usr/bin/python
# -*- coding: utf-8 -*-

########################
#Powered by kai.liang@i-soft.com.cn
#添加普华高性能模板和普华服务器安装光盘
#version v1.0
#usage: ./isoftTemplate.py
#######################

import MySQLdb
import urllib
import sys
import os


sql1 = "insert into install_media values(-2, '普华服务器操作系统', \
'/var/lib/isoft/shared/isos/isoft.iso', '30', '2016-11-02 17:33:27','python scripts', 'Cdrom')"
sql2 = "insert into install_media values(-3, '普华高性能模板', \
'/var/lib/isoft/shared/templates/isoft.img', '30', '2016-11-02 17:33:27','python scripts', 'Template')"
def downTemplate():
    url_iso = 'http://192.168.30.170/iSoft-3.1/iSoft-Server-OS-3.0-SP1-x86_64-201512282217.iso'
    local_iso = os.path.join('/var/lib/isoft/shared/isos', 'isoft.iso')
    print '普华服务器安装光盘正在下载，请稍后…'
    urllib.urlretrieve(url_iso,local_iso)
    print '普华服务器安装光盘已下载完毕。'
    url_img = 'http://192.168.30.170/iso-images/tmp/VMServer.img'
    local_img = os.path.join('/var/lib/isoft/shared/templates', 'isoft.img')
    print '普华高性能模板正在下载，请稍后…'
    urllib.urlretrieve(url_img,local_img)
    print '普华高性能模板已下载完毕。'
downTemplate()



def addIsoftTemplate():
    try:
        conn = MySQLdb.connect(host = 'localhost', \
				user = 'isoft', \
				passwd = 'smbee60f9',\
				db = 'smb')
	cur = conn.cursor()

	cur.execute(sql1)
	cur.execute(sql2)

	conn.commit()
        print '添加普华高性能模板成功！' 
    except Exception, e:
        print e
        print '非常遗憾，添加普华高性能模板失败！' 
        
    finally:
      cur.close()
      conn.close()
    return

addIsoftTemplate()
