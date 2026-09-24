import ollama

client = ollama.Client(host="http://127.0.0.1:11434")

system_prompt = r"""
你是一个字符串处理高手，可以按照我提供的要求对字符串做：
1. 验证
2. 抽取
3. 替换
动作
你的回复只包含动作的结果本身，不要带有任何额外信息。

要求，识别用户的意图
1. 如果用户意图是验证，则回复字符串True 或 False
2. 如果用户意图是抽取，则回复抽取结果本身，不要带有额外信息
   如果用户要求验证的是手机号，需要符合中国国内标准，如185、135、136、156等开头
3. 如果用户意图的替换，则回复替换结果本身，不要带有额外信息
"""


def ollama_chat(query):
    result = client.chat(
        model="qwen3:0.6b",  # 模型名称
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": query},
        ],
    )

    return result.message.content


s = input("输入手机号:")

r = ollama_chat(f"请将此手机号：{s}，进行验证，告知我是否是标准中国手机号码")

if r == "True":
    r = ollama_chat(f"请将此手机号：{s}，进行脱敏，中间4位数字替换为****")
    print(r)
else:
    print("请输入正确手机号")


# s = input("输入内容")

# msg = fr"""请对用户输入的内容做匹配，符合的回复True，不符合的回复False。
# 需求：用户提供一个邮箱，验证是否是标准邮箱

# 示例1，用户输入：abcd@qq.com 你的回复True
# 示例2，用户输入：asd@com  你的回复False

# 请回答，用户输入：{s}
# """

# r = ollama_chat(msg)
# print(r)
