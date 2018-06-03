#!/usr/bin/env python
# -*- coding: utf-8 -*-
import psutil

mem = psutil.virtual_memory()   # 使用psutil.virtual_memory方法获取内存完整信息

print(mem)
print(mem.total)   # 获取内存总数

print(mem.free)    # 获取空闲内存数

print(psutil.swap_memory())   # 获取SWAP分区信息