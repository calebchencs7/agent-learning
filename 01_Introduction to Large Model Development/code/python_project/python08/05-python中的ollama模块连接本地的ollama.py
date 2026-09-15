import ollama

# 连接本地的ollama模型
client = ollama.Client("http://127.0.0.1:11434")


# 选择模型或者角色，开始聊天
def get_ollama_response(prompt):
    result = client.chat(
        model="qwen3:0.6b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        stream=False
    )
    return result.message.content


if __name__ == '__main__':
    prompt = input("请输入您的问题：")
    response = get_ollama_response(prompt)
    print("AI助手的回答：", response)
