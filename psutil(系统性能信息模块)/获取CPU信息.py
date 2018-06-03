import psutil

# print(psutil.cpu_times(percpu=True))    # 使用cpu_time方法获取CPU完整信息，需要显示所有逻辑CPU信息
#
#
# print(psutil.cpu_times().user)    # 获取单项数据信息，如用户user的cpu时间比
#
# print(psutil.cpu_count())   # 获取cpu的逻辑个数，默认logical=True4
#
# print(psutil.cpu_count(logical=False))  # 获取CPU的物理个数
#
#
# cts = psutil.cpu_times()
# cputime = 0
# for item in cts:
#     if item != 0:
#         cputime = cputime + item
#
# print('用户时间：%f%%' % (cts.user / cputime * 100))

# print('内核时间：%f%%' % (cts.system / cputime * 100))
#
# print('空闲时间：%f%%' % (cts.idle / cputime * 100))
#

