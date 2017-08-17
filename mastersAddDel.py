#!/usr/bin/python
#coding:utf-8

########################
#Powered by kai.liang@i-soft.com.cn
#add or delete masters
#version v1.0
#usage: ./mastersAddDel.py -o add or del -n nums -h for help
#######################

import sqlite3
import os
import sys
import getopt

opts, args = getopt.getopt(sys.argv[1:], 'ho:n:')
option = 'add' #默认为添加集群
nums = 100  # 默认添加的集群数量

for op, value in opts:
    if op == '-o':
        option = value
    elif op == '-n':
        nums = value
        nums = int(nums)
    elif op == '-h':
        option = 'help'
        exit

DATA_DIR = "/var/lib/isoft"
DB_FILE = os.path.join(DATA_DIR, "smb-masterlist.data")

iptmp = '192.168.3.'
password = 'abc123'
nametmp = 'testcluster'
uuidtmp = '07eb8862-0a11-49d9-8be1-97c71050e10'
def addORdelMasters(num):
    try:
        conn = sqlite3.connect(DB_FILE)
        cur = conn.cursor()
        for i in range(1,num+1):
            ip = iptmp + str(i)
            name = nametmp + str(i)
            uuid = uuidtmp + str(i)
            if option == 'add':
                cur.execute("INSERT INTO master values('%s','%s','%s','%s') "\
% (ip, password,name, uuid)) 
            elif option == 'del':
                cur.execute("DELETE from master where uuid='%s'" % (uuid))
        conn.commit()
        print '%s %s Masters success!' % (option,num)
        return 0
    except Exception, e:
        print e
        print '%s %s Masters failed!' % (option,num)
        return 1
    finally:
        cur.close()
        conn.close() 
    return

if option == 'help':
    print 'usage: ./mastersAddDel.py -o add or del -n nums -h for help'
elif option == 'add' or option == 'del':
    result = addORdelMasters(nums)
    if result == 0:
        reVmslistd = os.system('/etc/init.d/vmslistd restart > /dev/null 2>&1')  #重启集群服务以便修改生效
