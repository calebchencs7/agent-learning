# 服务端需要选择一个运行端口
import socket

# 1.创建socket对象（类对象）
server = socket.socket(
    socket.AF_INET,  # 本质就是数字2， AF_INET IPv4地址（xxx.xxx.xxx.xxx）
    socket.SOCK_STREAM,  # 本质就是数字1， 代表TCP协议
)
# 2.选择IP地址和端口（IP地址就是自己电脑，端口随意，自定）
# socket对象的bind方法
server.bind(
    (
        # (IP,端口)
        # 127.0.0.1 表示自己电脑
        "127.0.0.1",
        7777,
    )
)

# 3.启动服务器，被客户端连接
# socket对象的listen()方法
# 启动后服务器就在7777端口等待客户端连接，客户端连接后，服务器就可以和客户端通信了
server.listen()
print("服务器当前运行在7777端口")


# 4.等待客户端接入
# socket对象的accept方法
# accept方法返回一个元组，返回2个元素
# # 元素1：客户端连接对象。此对象记录了客户端的一切特征，和客户端通讯使用这个对象
# # 元素2：记录了客户端的IP和端口，可以自行取用
# # accept()方法是阻塞式， 如果客户端不接入，代码就卡在这里

client, client_info = server.accept()  # 阻塞式等待客户端接入

# 5.给客户端发送消息
# socket对象的send方法
# 发送和接收都是2进制
client.send("I am the server".encode("UTF-8"))  # 服务器向客户端发消息

# 6.接收客户端的消息
# socket对象的recv方法
# 接收的也是2进制
# 1024，表示一次最多接收多少字节（byte），1024表示1024Byte == 1KB
recv_data = client.recv(1024)  # 阻塞方法，不收到消息就不向下执行
print(f"收到客户端的数据：{recv_data.decode('UTF-8')}")


# 7.主动关闭连接
# socket对象的close方法
client.close()  # 关闭客户端连接
