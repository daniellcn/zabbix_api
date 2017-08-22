#!/bin/env python
from pyzabbix import ZabbixAPI

#graphs_list =[{"resourceid": "612"}]

#coding:utf-8
host_all = []
zapi = ZabbixAPI("http://zabbix2.800best.com/")
zapi.login("Admin","zabbix")
hosts = zapi.host.get()
hostgroups=zapi.hostgroup.get()
templates=zapi.template.get()

#print hostgroups
for group in hostgroups:
    print group['groupid'] + ' : ' + group['name']
for host in hosts:
    host_all.append(host['name'])
    print host['hostid']+' : ' +host['name']
for template in templates:
    #host_all.append(host['name'])
    print template['templateid']+' : ' +template['name']


aa = {
            "host": "Test Server111",
            "groups": [{"groupid":"8"}],
            "templates": [{"templateid":"10104"}],
            "interfaces":[
                {
                    "type":1,
                    "main":1,
                    "useip":1,
                    "ip":"192.168.33.111",
                    "dns":"",
                    "port":"10050"
                 }
            ],
            "status":0
}

#zapi.screen.create(name='testscreen',hsize=4,vsize=4)
zapi.host.create(aa)
