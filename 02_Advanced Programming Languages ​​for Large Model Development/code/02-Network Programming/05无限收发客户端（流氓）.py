"""
免责声明：本代码纯学习用途
# DDos攻击
"""

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("127.0.0.1", 7777))

count = 1
while True:
    # client.send(f"第{count}条消息".encode("UTF-8"))
    client.send(("hello viola").encode("UTF-8"))
    count += 1
