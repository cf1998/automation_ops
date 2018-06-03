#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psutil
import datetime

print(psutil.users())   # 使用psutil.users方法返回当前登陆系统的用户信息

print(psutil.boot_time())  # 使用psutil.boot_time方法获取开机时间，以Linux时间戳格式返回

# 转化成自然时间格式
print(datetime.datetime.fromtimestamp(psutil.boot_time()).strftime('%Y-%m-%d %H: %M: %S'))