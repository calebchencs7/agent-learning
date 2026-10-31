import ollama

# 创建ollama对象
ollama_client = ollama.Client(host="http://127.0.0.1:11434/")

# 直接聊天
res = ollama_client.chat(
    model="qwen3:0.6b",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "AI市场的前景如何？能持续几年"},
    ],
)


# 获取ai回复的内容

print(res.message.content)
