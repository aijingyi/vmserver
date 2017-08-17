#!/usr/bin/python
#coding:utf-8

########################
#Powered by kai.liang@i-soft.com.cn
#添加光盘
#version v1.0
#usage: ./addCdrom.py
#######################

import MySQLdb
import urllib
import sys
import os


#下载光盘iso通用函数
def downCdrom(iso, url, local):
    print '光盘镜像 %s 正在下载，请稍后…' %(iso)
    urllib.urlretrieve(url,local)
    print '光盘镜像 %s 已下载完毕。' %(iso)


def connSql(name):
    try:
	#创建数据库对象
        conn = MySQLdb.connect(host = 'localhost', \
				user = 'isoft', \
				passwd = 'smbee60f9',\
				db = 'smb')
	#创建游标对象
	cur = conn.cursor()

        sql1 = "insert into install_media(name, file, os_id, time, description, type) values( '%s','%s','%s','%s','%s','%s')"
	cur.execute(sql1 %(name))

	conn.commit()
         
    except Exception, e:
        print e
        
    finally:
      cur.close()
      conn.close()
    return

def server3_1():
    iso = 'iSoftServerOS-3.1'
   # url = 'http://192.168.30.170/iSoft-3.1/iSoft-Server-OS-3.0-SP1-x86_64-201512282217.iso'
    url = 'http://192.168.32.48/iso/Win8PE.iso'
    local = os.path.join('/var/lib/isoft/shared/isos', 'iSoft-Server-OS-3.0-SP1.iso')
    cdromList = (iso, '/var/lib/isoft/shared/isos/iSoft-Server-OS-3.0-SP1.iso', '30', '2016-11-02 17:33:27', 'by python scripts', 'Cdrom')
    downCdrom(iso, url, local)
    connSql(cdromList)
    print '成功添加光盘镜像 %s!' %(iso)

def windows7():
    iso = 'Windows7_x64_sp1'
    url = 'http://192.168.32.48/iso/Win8PE.iso'
    local = os.path.join('/var/lib/isoft/shared/isos', 'Windows7_x64_sp1.iso')
    cdromList = (iso, '/var/lib/isoft/shared/isos/Windows7_x64_sp1.iso', '1', '2016-11-02 17:33:27', 'by python scripts', 'Cdrom')
    downCdrom(iso, url, local)
    connSql(cdromList)
    print '成功添加光盘镜像 %s!' %(iso)

def windows7_32():
    iso = 'Windows7_x86_sp1'
    url = 'http://192.168.32.48/iso/Win8PE.iso'
    local = os.path.join('/var/lib/isoft/shared/isos', 'Windows7_x86_sp1.iso')
    cdromList = (iso, '/var/lib/isoft/shared/isos/Windows7_x86_sp1.iso', '1', '2016-11-02 17:33:27', 'by python scripts', 'Cdrom')
    downCdrom(iso, url, local)
    connSql(cdromList)
    print '成功添加光盘镜像 %s!' %(iso)


def windows8():
    iso = 'Windows8_x64'
    url = 'http://192.168.32.48/iso/Win8PE.iso'
    local = os.path.join('/var/lib/isoft/shared/isos', 'Windows8_x86.iso')
    cdromList = (iso, '/var/lib/isoft/shared/isos/Windows8_x86.iso', '2', '2016-11-02 17:33:27', 'by python scripts', 'Cdrom')
    downCdrom(iso, url, local)
    connSql(cdromList)
    print '成功添加光盘镜像 %s!' %(iso)

def windows10():
    iso = 'Windows10_x64'
    url = 'http://192.168.32.48/iso/Win8PE.iso'
    local = os.path.join('/var/lib/isoft/shared/isos', 'WindowsXP_x64.iso')
    cdromList = (iso, '/var/lib/isoft/shared/isos/Windows10_x64.iso', '5', '2016-11-02 17:33:27', 'by python scripts', 'Cdrom')
    downCdrom(iso, url, local)
    connSql(cdromList)
    print '成功添加光盘镜像 %s!' %(iso)

def winserv2003():
    iso = 'WindowsServer2003'
    url = 'http://192.168.32.48/iso/Win8PE.iso'
    local = os.path.join('/var/lib/isoft/shared/isos', 'WindowsXP_sp3.iso')
    cdromList = (iso, '/var/lib/isoft/shared/isos/WindowsXP_sp3.iso', '20', '2016-11-02 17:33:27', 'by python scripts', 'Cdrom')
    downCdrom(iso, url, local)
    connSql(cdromList)
    print '成功添加光盘镜像 %s!' %(iso)

def windows_xp():
    iso = 'WindowsXP_sp3'
    url = 'http://192.168.32.48/iso/Win8PE.iso'
    local = os.path.join('/var/lib/isoft/shared/isos', 'WindowsXP_sp3.iso')
    cdromList = (iso, '/var/lib/isoft/shared/isos/WindowsXP_sp3.iso', '20', '2016-11-02 17:33:27', 'by python scripts', 'Cdrom')
    downCdrom(iso, url, local)
    connSql(cdromList)
    print '成功添加光盘镜像 %s!' %(iso)

#server3_1()
#windows7()
#windows7_32()
#windows8()
windows10()
#windows_xp()

