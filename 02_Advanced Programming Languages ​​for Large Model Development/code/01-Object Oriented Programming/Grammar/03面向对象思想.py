"""
面向对象编程：
1. 设计一个类
2. 基于类创建具体的对象（变量）
3. 由对象记录数据（属性记录），由对象执行实体的行为（函数方法）
"""

import platform
import subprocess
import time


# 1. 设计闹钟类
class Clock:
    id = None  # 记录闹钟的序列号
    price = None  # 记录闹钟的零售价

    def ring(self):  # 设计闹钟的响铃功能
        if platform.system() == "Windows":
            import winsound

            winsound.Beep(2000, 3000)
        else:
            # macOS 使用系统自带的提示音和播放器
            subprocess.run(
                ["afplay", "/System/Library/Sounds/Glass.aiff"],
                check=True,
            )


# 2. 生产对象（上流水线）
clock1 = Clock()
clock2 = Clock()

# 3. 对象干活
# 对象完成属性的记录
clock1.id = 1
clock1.price = 19.99  # 在商店A 卖19.99
print(f"clock1 id：{clock1.id} 价格：{clock1.price}")
clock2.id = 2
clock2.price = 24.99  # 在黑店就卖 24.99
print(f"clock1 id：{clock2.id} 价格：{clock2.price}")

clock1.ring()


time.sleep(3)
clock2.ring()
