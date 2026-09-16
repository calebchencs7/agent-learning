"""
无限和服务器发送消息
发送的每一条消息都是input输入
当输入消息为bye的时候，结束连接
"""

import socket

# 获取socket对象
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接服务器
client.connect(('127.0.0.1', 12345))

# 无限发送流程
while True:
    msg = input("准备发什么？")
    client.send(msg.encode("utf-8"))

    if msg == 'bye':
        break
