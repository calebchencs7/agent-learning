"""
每接入一个客户端，就会创建一个新的进程来处理该客户端的请求。
Each time a client connects, a new process is created to handle the client's requests.
2.每个子进程里服务端无限收，直到客户端发来‘bye’，才close
"""

import socket
import multiprocessing as mp


# 定义处理客户端请求的函数
def handle_client(client, client_info):
    print(f"客户端{client_info}接入")
    # 发消息给客户端
    client.send("接收到了客户端发的消息".encode("UTF-8"))
    # 无限循环，直到客户端发来‘bye’，才close
    while True:
        try:
            recv_data = client.recv(1024)
            msg = recv_data.decode('utf-8')
            if not recv_data:
                print(f"客户端{client_info}断开连接")
                break
            print(f"收到客户端{client_info}发来的消息：{msg}")
            if recv_data.decode('utf-8') == 'bye':
                print(f"客户端{client_info}发送了bye，关闭连接")
                break
        except Exception as e:
            print(f"{client_info}消息错误，停止服务")
            break
    client.close()


if __name__ == '__main__':
    # 创建socket 服务端对象
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # bind
    server.bind(("0.0.0.0", 7777))
    # listen
    server.listen()  # 监听端口

    # 等待客户端
    while True:
        client, client_info = (
            server.accept()
        )  # accept()方法会阻塞，直到有客户端连接进来

        # 创建一个新的进程来处理该客户端的请求
        p = mp.Process(target=handle_client, args=(client, client_info))
        p.start()
