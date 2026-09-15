import ollama

# 连接本地的ollama模型
client = ollama.Client("http://127.0.0.1:11434")


# 选择模型或者角色，开始聊天
def get_ollama_response(messages):
    result = client.chat(
        model="qwen3:0.6b",
        messages=messages,
        stream=False
    )
    return result.message.content


if __name__ == '__main__':
    prompt = input("请输入您的问题：")
    messages = [
        {
            "role": "user",
            "content": prompt
        }
    ]
    response = get_ollama_response(messages)
    print("AI助手的回答：", response)
