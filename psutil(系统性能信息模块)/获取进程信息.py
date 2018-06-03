#!/usr/bin/env python
# -*- coding: utf-8 -*-
import psutil
print(psutil.pids())   # 列出所有进程PID

p = psutil.Process(953) # 实例化一个Process对象，参考为一个进程的PID
print(p.name() )# 进程名字

print(p.exe())  # 进程bin路径

print(p.cwd())   # 进程工作目录绝对路径

print(p.status())  # 进程状态

print(p.create_time())  # 进程创建时间，时间戳格式

print(p.uids())    # 查看进程uid信息

print(p.gids())  # 进程gid信息

print(p.cpu_times())   # 进程CPU时间信息，包括user,system两个CPU时间

print(p.cpu_affinity())  # get进程CPU亲和度，如要设置进程CPU亲和度，将CPU号作为参数即可

print(p.memory_percent())  # 进程内存使用率

print(p.memory_info)   # 进程内存res,vms信息

print(p.io_counters())  # 进程IO信息，包括读写IO数及字节数

print(p.connections())  # 返回打开进程socket的namedutples列表，包括fs,family,laddr等信息

print(p.num_threads())  # 进程开启的线程数


