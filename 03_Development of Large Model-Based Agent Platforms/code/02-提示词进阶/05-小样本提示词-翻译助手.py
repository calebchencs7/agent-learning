import ollama
from openai import OpenAI


def get_translate_results(text):
    # 编写系统提示词
    SYSEM_PROMPT = """你是一个翻译专家，请将用户输入的英文翻译成中文。
        示例：
        英文：I Love you.
        中文 我爱你
        现在开始翻译用户输入的内容
    """

    # 创建客户端对象
    client = OpenAI(
        api_key="ollama",
        base_url="http://127.0.0.1:11434/v1",
    )

    # 直接聊天
    res = client.chat.completions.create(
        # 模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
        model="qwen3:0.6b",
        messages=[
            {"role": "system", "content": SYSEM_PROMPT},
            {"role": "user", "content": text},
        ],
        stream=False,
        temperature=0.7,
    )
    return res.choices[0].message.content


if __name__ == "__main__":
    text = "Hello world!"
    translate = get_translate_results(text)
    print(translate)


# 结果：Autumn brings cool weather and bright sunshine.
