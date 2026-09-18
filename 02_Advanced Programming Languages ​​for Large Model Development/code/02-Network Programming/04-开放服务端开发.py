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
server.bind(("0.0.0.0", 7777))

# 启动服务器
server.listen()  # 监听端口

# 等待客户端
while True:
    client, client_info = server.accept()  # accept()方法会阻塞，直到有客户端连接进来
    print(f"客户端{client_info}接入")
    # 发消息给客户端
    client.send("接收到了客户端发的消息".encode("UTF-8"))
    # 等待客户端消息
    try:
        recv_data = client.recv(1024)
        print(f"收到客户端{client_info}发来的消息：{recv_data.decode('utf-8')}")
    except Exception as e:
        print(f"{client_info}消息错误，停止服务")
    finally:
        client.close()
