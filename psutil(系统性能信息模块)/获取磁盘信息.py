#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psutil

print(psutil.disk_io_counters())   # 使用 psutil.disk_io_counters方法获取磁盘完整信息

print(psutil.disk_usage('/'))  # 使用psutil.disk_usage方法获取分区(参数)的使用情况

print(psutil.disk_io_counters())  # 使用psutil.disk_io_counters获取磁盘总的IO个数

print(psutil.disk_io_counters(perdisk=True))  # "perdisk=True"参数获取单个分区IO个数