import socket

# 1. 创建socket对象（IP4、TCP）
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2. 发起连接（客户端是主动方）（服务器需要提前运行好）
client.connect(  # 背后就是三次握手
    ("127.0.0.1", 7777)  # IP和端口都要指定服务器的，不要乱填
)
# 3. 发送或接收 （send、recv）
# 先收一条
recv_data = client.recv(1024)
print(f"收到服务器的回复：{recv_data.decode('utf-8')}")

# 再发一条
client.send("我爱宋小佳❤️".encode("UTF-8"))
# 4. 关闭
client.close()  # 背后就是四次挥手
