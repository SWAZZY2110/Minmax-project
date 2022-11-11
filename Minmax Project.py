#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 19:38:31 2022

@author: priyankadas
"""

import matplotlib .pyplot as plt
import psutil as p

name_list = []
percent_list = []
minmax_list = []
max_cpu = 0
min_cpu = 0
count = 0

for process in p.process_iter():
    count = count + 1
    if count <= 2:
        print(process)
        name = process.name()
        cpu_usage = p.cpu_percent()
        name_list.append(name)
        percent_list.append(cpu_usage)
        print(name_list)
        print(percent_list)
min_cpu = min(percent_list)
max_cpu = max(percent_list)
minmax_list.append(min_cpu)
minmax_list.append(max_cpu)
plt.figure(figsize=(15, 7))
plt.xlabel("Applications")
plt.ylabel("Usage")
plt.bar(name_list, minmax_list, width = 0.6, color = ("Red","Orange"))
plt.show()