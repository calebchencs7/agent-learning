"""
开发一个服务器，可以和无数的客户端通讯
每一次通讯只服务1个客户端，剩余的排队
"""

import socket

# 创建socket 服务端对象
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 选择绑定IP和端口
# 0.0.0.0       表示自己电脑，同时表示允许任何人连接
# 127.0.0.1     表示自己电脑，同时表示只允许自己电脑内的程序连接
server.bind(("127.0.0.1", 7777))

# 启动服务器
server.listen()

# 等待客户端
while True:
    client, client_info = server.accept()
    print(f"客户端{client_info}接入")
    # 发消息给客户端
    client.send("hello client".encode("UTF-8"))
    # 等待客户端消息
    while True:
        try:
            recv_data = client.recv(1024)
            print(f"收到客户端{client_info}发来的消息：{recv_data.decode('utf-8')}")
        except Exception as e:
            print(f"{client_info}消息不对，停止服务")
            break

    client.close()
