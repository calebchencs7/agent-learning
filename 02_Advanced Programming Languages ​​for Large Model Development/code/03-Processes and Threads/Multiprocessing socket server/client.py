# 客户端可以一直输入消息给server
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 7777))

while True:
    msg = input("请输入要发送的消息：")
    client.send(msg.encode("UTF-8"))
    if msg == "bye":
        break
