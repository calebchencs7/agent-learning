from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

# 创建客户端对象
client = OpenAI(
    api_key=os.getenv("BAILIAN_API_KEY"),
    base_url="https://ws-9p62epy2octdhspq.cn-beijing.maas.aliyuncs.com/compatible-mode/v1",
)

SYSTEM_PROMPT = [
    "你是信息抽取助手。请从下面的'''嵌套文本中提取研究背景、方法、结果和结论。''' ",
    "你是学术写作助手。请根据以下'''嵌套文本中要点写一段逻辑清晰的摘要草稿。''' ",
    "你是学术语言编辑。请将以下'''嵌套文本中的摘要改得更简洁、正式，保留原有事实和数值，不添加未经验证的结论。'''",
]

USER_PROMPT = []


def get_result(text):
    USER_PROMPT = [f"'''{text}'''"]
    for i in range(3):

        completion = client.chat.completions.create(
            # 模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
            model="qwen3.8-flash",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT[i]},
                {"role": "user", "content": USER_PROMPT[i]},
            ],
        )
        print(f"第{i + 1}次的系统提示词：{SYSTEM_PROMPT[i]}")
        print(f"第{i + 1}次的用户提示词：{USER_PROMPT[i]}")
        print(f"第{i + 1}次的结果：{completion.choices[0].message.content}")

        # 获取结果
        USER_PROMPT.append(completion.choices[0].message.content)
        print('----------------------------------------------------------------------')

    return USER_PROMPT[-1]  # 返回最后一个结果


if __name__ == "__main__":
    text = """
    近年来，深度学习在自然语言处理中的应用快速发展。本文提出一种基于注意力机制的改进模型，并在文本分类任务中进行实验。
    实验结果显示，该方法的准确率比传统方法提高了 5%。研究认为，注意力机制提升了模型的表达能力。
    """
    data = get_result(text)
    print(data)

