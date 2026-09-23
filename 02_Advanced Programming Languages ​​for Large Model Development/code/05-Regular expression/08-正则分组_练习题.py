# 1. 将手机号替换为1*********1  中间9个数字为*
#
# 2. 微博超话  #.....#， 抽取2个#的内容输出
#
# 3. IP地址xxx.xxx.xxx.xxx，输出中间第二个xxx和第三xxx，分开输出
#
# 4. 网址：http://www.qq.com，分别输出
#     协议，即http或https
#     域名，即qq.com
#     协议http或https
#     域名支持 qq.com sina.com itheima.com itcast.cn
import re


def demo1():
    # 将手机号替换为1*********1  中间9个数字为*
    s = "18500001116"
    p = r"(\d)\d{9}(\d)"

    r = re.sub(p, r"\1*********\2", s)
    print(r)


def demo2():
    # 微博超话  #.....#， 抽取2个#的内容输出
    s = "今日热点#周杰轮发新歌了#哈哈哈"

    p = r"#(\w+)#"

    r = re.search(p, s)
    print(r.group(1))


def demo3():
    # IP地址xxx.xxx.xxx.xxx，输出中间第二个xxx和第三xxx，分开输出
    s = "192.168.88.101"
    p = r"^\d{1,3}\.(\d{1,3})\.(\d{1,3})\.\d{1,3}$"

    r = re.match(p, s)
    print("part2:", r.group(1))
    print("part3:", r.group(2))


def demo4():
    r"""
    网址：http://www.qq.com，分别输出
    协议，即http或https
    域名，即qq.com
    协议http或https
    域名支持 qq.com sina.com itheima.com itcast.cn
    """
    s = "https://www.itcast.cn"
    p = r"^(https?)://www\.(qq\.com|sina\.com|itheima\.com|itcast\.cn)$"

    r = re.match(p, s)
    print("协议：", r.group(1))
    print("域名：", r.group(2))


demo4()
