"""
可以接收任意数量客户端接入，每一次只服务1个客户端
和被服务的客户端沟通的时候，可以无限接收客户端发来的消息
直到客户端发来`bye`，服务器断开和这个客户端的连接
"""
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind
server.bind(('127.0.0.1', 12345))

# listen
server.listen()

while True:
    print("等待客户端接入")
    client, client_info = server.accept()
    print(f"客户端{client_info}接入")

    while True:
        msg = client.recv(1024)
        print(f"收到客户端{client_info}的消息：{msg.decode('utf-8')}")

        if msg.decode('utf-8') == 'bye':
            client.close()
            print(f"关闭和客户端{client_info}的连接")
            break
