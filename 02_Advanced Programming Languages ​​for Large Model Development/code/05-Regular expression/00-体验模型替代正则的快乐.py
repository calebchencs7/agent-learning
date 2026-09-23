import ollama
import json

client = ollama.Client(host="http://127.0.0.1:11434")

content = """
你是一个信息提取的助手，帮助我从文本中抽取关键信息，并组装为JSON格式字符串返回给我。
我将给你1个示例，如下：
用户输入：大家好，我叫渣渣辉，今年23岁，来自安徽省合肥市，很高兴见到大家
你的输出：{"name": "渣渣辉", "age": 23, "province": "安徽省", "city": "合肥市"}

要求，直接给出输出，不要带有额外信息。
"""


def ollama_chat(query):
    result = client.chat(
        model="qwen3:0.6b",  # 模型名称
        messages=[
            {"role": "system", "content": content},
            {"role": "user", "content": query},
        ],
    )

    return result.message.content


str1 = "哎，今年都33岁了，哦对了我叫小曹，来自安徽省阜阳市，大家好"
str2 = (
    "嘿嘿，我才18岁哦，来自美丽的安徽省，我居住的地方是合肥市，你们可以叫我王大锤，嘻嘻"
)

r1 = ollama_chat(str1)
d1 = json.loads(r1)
print(d1, type(d1))

print("-" * 20)
r2 = ollama_chat(str2)
d2 = json.loads(r2)
print(d2, type(d2))
