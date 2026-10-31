import json

d1 = {
    '日期': ['2023-01-10'],
    '股票名称': ['古哥-D[EOOE]美股'],
    '开盘价': ['100美元'],
    '收盘价': ['102美元'],
    '成交量': ['520000'],
}
print(d1)
print(type(d1))


# 字典转化为json字符串
json_str = json.dumps(d1, ensure_ascii=False)
print(json_str)
print(type(json_str))


# json 字符串再转为字典
d2 = json.loads(json_str)
print(d2)
print(type(d2))
