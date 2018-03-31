#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import os
import subprocess
import re

hosts = []

low_port = 1
max_port = 65535

ports = [22, 23, 80, 999]

_ip = '192.168.1.'
hostbit = 0

while hostbit <= 255:
    ping = subprocess.Popen('ping -c 1 -t 0 ' + _ip + str(hostbit), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    (out, error) = ping.communicate()
    out = str(out)
    find = re.search('Destination host unreachable', out)
    if find is None:
        hosts.append(_ip + str(hostbit))
    hostbit = hostbit + 1

print '+---------------------------------+'
print '|     hosts and ports found :     |'
print '+---------------------------------+'

for host in hosts:
    try:
        (name, alias, addresslist) = socket.gethostbyaddr(host)
    except:
        name = None
    if name != None:
        print "[+] " + host + " | " + name
        for port in ports:
            try:
                test_port = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                test_port.settimeout(0.1)
                res = test_port.connect_ex((host, port))
                if res != 0:
                    print " [*] Port " + str(port) + " is open !"
                res.close()
            except:
                pass
