import ollama
from openai import OpenAI

# 创建客户端对象
client = OpenAI(
    api_key="ollama",
    base_url="http://127.0.0.1:11434/v1",
)

res = client.chat.completions.create(
    # 模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
    model="qwen3:0.6b",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "你是谁？"},
    ],
)


print(res)
