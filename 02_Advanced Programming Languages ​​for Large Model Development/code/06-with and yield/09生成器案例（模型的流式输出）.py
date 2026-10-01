from unittest import result

import ollama

client = ollama.Client(host="http://127.0.0.1:11434")


# def ollama_chat(query):
#     result = client.chat(
#         model="qwen3:0.6b",  # 模型名称
#         messages=[{"role": "user", "content": query}],
#         stream=False,  # 不开启流
#     )

#     print(result)
#     print(type(result))  # <class 'ollama._types.ChatResponse'>


# ollama_chat("你能干嘛")


def ollama_chat(query):
    result = client.chat(
        model="qwen3:0.6b",  # 模型名称
        messages=[{"role": "user", "content": query}],
        stream=True,  # 开启流
    )
    print(type(result))  # <class 'generator'>

    for chunk in result:
        if not chunk.message.content:
            print(chunk.message.thinking, end="")
        else:
            print(chunk.message.content, end="")


ollama_chat("你能干嘛,回答字数至少400字")
