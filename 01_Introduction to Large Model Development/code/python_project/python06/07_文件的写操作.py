# 需求: 已知列表中存储了['file', 'open', 'close', 'read', 'write']
# 文件的打开
f = open('test.txt', 'a', encoding='utf-8')
my_list = ['file', 'open', 'close', 'read', 'write']
for word in my_list:
    # 文件的写入
    f.write(word + '\n')
# 文件的关闭
f.close()
