# import方式
import 模块1

模块1.show()
print(模块1.get_sum1(1, 2))
print('========================================================')

# from import方式
from 模块2 import show, get_sum
from 模块1 import show

show()
print(get_sum(1, 2))
print('==========================================================')

# 注意: from 模块名 import * 这种方式可以配合__all__列表使用
from 模块1 import *

show()
print(get_sum1(2, 1))
# print(get_diff(2, 1)) # 报错,因为模块中__all__列表没有指定这个函数
print('========================================================')

# import 方式 导入包中模块
import 包.模块3 as mk3

mk3.func1()
print('========================================================')

# from import方式 导入包中模块
# from 包 import 模块4
#
# 模块4.func1()
print('========================================================')

# from import方式 导入包中模块
# from 包.模块4 import func2
#
# func2()


print('========================================================')
# from import方式 导入包中模块
# from 包 import 模块3,模块4
# 模块3.func1()
# 模块4.func1()
print('========================================================')
# from import方式 导入包中模块
from 包 import *

模块3.func1()
# 模块4.func1() # 报错,因为__init__.py文件中的__all__列表没有没有指定这个模块
