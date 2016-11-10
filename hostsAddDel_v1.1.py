#!/usr/bin/python
# -*- coding: utf-8 -*-

########################
#Powered by kai.liang@i-soft.com.cn
#add or delete hosts
#version v1.1
#usage: ./hostAddDel.py -o add or del -n nums -h for help
#2016-11-02 修改了添加的虚拟主机与原有主机重复id时导致添加失败的问题
#######################

import MySQLdb
import getopt
import sys

opts, args = getopt.getopt(sys.argv[1:], 'ho:n:')
option = 'add' #默认为添加除集群
nums = 20  # 添加的集群数量

for op, value in opts:
    if op == '-o':
        option = value
    elif op == '-n':
        nums = value
        nums = int(nums)
    elif op == '-h':
        option = 'help'

uuidtmp = '07eb8862-0a11-49d9-8be1-97c71050e10'
hostnametmp = 'testHost'
iptmp = '192.168.4.'
physical_cpu_num = '1'
logical_cpu_num = '4'
cpu_model = 'GenuineIntel'
sql1 = "insert into host(uuid, hostname, ip) values('%s', '%s', '%s')"
sql2 = "delete from host where hostname='%s'"
def addORdelHosts(num):
    try:
        conn = MySQLdb.connect(host = 'localhost', \
				user = 'isoft', \
				passwd = 'smbee60f9',\
				db = 'smb')
	cur = conn.cursor()
	
	for i in range(1, num + 1):
	    uuid = uuidtmp + str(i)
            hostname = hostnametmp + str(i)
	    ip = iptmp + str(i) 
            if option == 'add':
	        cur.execute(sql1 %(uuid, hostname, ip))
            elif option == 'del':
	        cur.execute(sql2 %(hostname))
	
	conn.commit()
        print '%s %s hosts success!' % (option,num)
    except Exception, e:
        print e
        print '%s %s hosts failed!' % (option,num)
        
    finally:
      cur.close()
      conn.close()
    return

if option == 'help':
    print 'usage: ./hostAddDel.py -o add or del -n nums -h for help'
elif option == 'add' or 'del':    
    addORdelHosts(nums)
