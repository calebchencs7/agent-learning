# 方式1: import 模块名
import time
import time as tm

print('开始')
time.sleep(1)
print('结束')
print(time.localtime())
print('==============================')

# 方式2: from 模块名 import 功能名
from time import sleep
from time import sleep as sl
from time import *

print('---开始---')
sleep(1)
print('---结束---')
print(localtime())
