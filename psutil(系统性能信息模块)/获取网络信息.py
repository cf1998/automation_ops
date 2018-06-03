#!/usr/bin/env python
# -*- coding: utf-8 -*-
import psutil

print(psutil.net_io_counters())  # 使用psutil.net_io_counters获取网络总的IO信息默认#pernice=False

print(psutil.net_io_counters(pernic=True))# pernice=True输出每个网络接口的IO信息