#!/usr/bin/python 
#coding:utf-8

########################
#Powered by kai.liang@i-soft.com.cn
#get infomation of host
#version v1.0
#usage: ./hostInfo.py
#使用本脚本可以输出主机基本信息和集群主机使用分析并与
#客户端相关信息进行对比。
#######################

from commands import getstatusoutput
import socket

# get host cpu count and cpu frequence

hostname = socket.gethostname()
def hostIp():
    file = open("/etc/sysconfig/network-scripts/ifcfg-smbebr","r")
    for line in file.readlines():
        if line.startswith("IPADDR"):
            ip = line.split()[0][7:]
    return ip

def cpuUsage():
    rc, out = getstatusoutput("top -b -n1 -d0")
    line = out.split("\n")[2]
    return 100 - int(round(float(line.split(",")[3].strip()[:-3])))

def cpuInfo():
    cpuCount = 0
    cpuFrequence = 0
    file = open("/proc/cpuinfo", "r")
    for line in file.readlines():
        if line.startswith("processor"):
            cpuCount += 1
        if line.startswith("cpu MHz"):
            cpuFrequence = int(float(line.split(":")[1].strip()))
        if line.startswith("vendor_id"):
            cpuVendor = line.split(":")[1].strip()
        if line.startswith("model name"):
            cpuModel = line.split(":")[1].strip()
    file.close()
    return cpuCount, cpuVendor, cpuModel
def memUsage():
    total = 0.0
    free = 0.0
    cached = 0.0

    file = open("/proc/meminfo", "r")
    for line in file.readlines():
        if line.startswith("MemTotal:"):
            total = float(line.split(":")[1].strip()[:-3])
        if line.startswith("MemFree:"):
            free = float(line.split(":")[1].strip()[:-3])
        if line.startswith("Cached:"):
            cached = float(line.split(":")[1].strip()[:-3])
    
    mem = total / 1000.0 /1000.0
    used = (total - free -cached) / 1000.0 / 1000.0
    usage =  int(round((total - free - cached) / total * 100))
    return mem, used, usage
def diskUsage():
    usage = 0.0

    rc, out = getstatusoutput("export LANGUAGE=C;/bin/df --direct /var/lib/isoft")
    line = out.split("\n")[1]
    used = int(line.split()[2]) / 1024.0 /1024.0
    usage = int(round(float(line.split()[4][:-1])))
    disk = (int(line.split()[2]) + int(line.split()[3])) / 1024.0 /1024.0
    return usage, used, disk
mem , memused, memusage = memUsage()
ip = hostIp()
diskusage, diskused, disk = diskUsage()
cpuCount, cpuVendor, cpuModel = cpuInfo()
cpuUsage = cpuUsage()

def printHostInfo():
    print '使用本脚本可以输出主机基本信息和集群主机使用分析并与\n客户端相关信息进行对比。'
    print '#########################'
    print '主机基本信息'
    print '主机名称：%s' %(hostname)
    print 'IP地址：%s' %(ip)
    print 'CPU核数：%s' %(cpuCount)
    print 'CPU供应商：%s' %(cpuVendor)
    print 'CPU型号：%s' %(cpuModel)
    print '内存:【%s%%】已用 %sGB/合计 %sGB' %(memusage, memused, mem)
    print '存储：【%s%%】已用 %sGB/合计 %sGB' %(diskusage, diskused, disk)
    print '#########################'
    print '集群主机使用分析'
    print 'CPU占用率：%s%%' %(cpuUsage)
    print '内存占用率：%s%%' %(memusage)
    print '磁盘占用率：%s%%' %(diskusage)
    print '#########################'
info = printHostInfo()


