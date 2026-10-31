"""
一.文本抽取
1.参考文本
    [{
        'content': '2023-01-10，股市震荡。股票古哥-D[EOOE]美股今日开盘价100美元，一度飙升至105美元，随后回落至98美元，最终以102美元收盘，成交量达到520000。',
        'answers': {
            '日期': ['2023-01-10'],
            '股票名称': ['古哥-D[EOOE]美股'],
            '开盘价': ['100美元'],
            '收盘价': ['102美元'],
            '成交量': ['520000'],
        }
    }]

2.验证文本
'2025-02-15，寓意吉祥的节日，股票佰笃[BD]美股开盘价10美元，虽然经历了波动，但最终以13美元收盘，成交量微幅增加至460,000，投资者情绪较为平稳。',
 '2025-04-05，市场迎来轻松氛围，股票盘古(0021)开盘价23元，尽管经历了波动，但最终以26美元收盘，成交量缩小至310,000，投资者保持观望态度。',
"""

"""
核心思路:
1.初始化历史提示词（System + user + assistant）
2.调用模型完成文本抽取（传入验证文本）
"""


# 0. 导包
from openai import OpenAI
import json
import os
from dotenv import load_dotenv

load_dotenv()


# TODO 1. 初始化历史提示词（System + user + assistant）
def init_history_prompt():
    examples = [
        {
            'content': '2023-01-10，股市震荡。股票古哥-D[EOOE]美股今日开盘价100美元，一度飙升至105美元，随后回落至98美元，最终以102美元收盘，成交量达到520000。',
            'answers': {
                '日期': ['2023-01-10'],
                '股票名称': ['古哥-D[EOOE]美股'],
                '开盘价': ['100美元'],
                '收盘价': ['102美元'],
                '成交量': ['520000'],
            },
        }
    ]
    # 准备系统提示词
    schema = {'金融': ['日期', '股票名称', '开盘价', '收盘价', '成交量']}

    system_prompt = f"""你是一个专业的文本抽取模型，你需要根据提供的文本内容，从文本中抽取指定的信息。抽取的信息包括{schema['金融']}"""
    history_prompt = [{'role': 'system', 'content': system_prompt}]

    # 系统提示词拼接小样本
    for example in examples:
        history_prompt.append({'role': 'user', 'content': example['content']})
        history_prompt.append(
            {
                'role': 'assistant',
                'content': json.dumps(example['answers'], ensure_ascii=False),
            }
        )

    return history_prompt


# TODO 2.调用模型完成文本信息抽取（传入验证文本）
client = OpenAI(
    api_key=os.getenv("BAILIAN_API_KEY"),
    base_url="https://ws-9p62epy2octdhspq.cn-beijing.maas.aliyuncs.com/compatible-mode/v1",
)


# 定义API接口
def extract_model(texts):
    results = []
    for text in texts:
        completion = client.chat.completions.create(
            # 模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
            model="qwen-plus",
            messages=init_history_prompt() + [{'role': 'user', 'content': text}],
        )
        result = completion.choices[0].message.content
        print(f"文本: {text} -> 抽取结果: {result}")
        results.append(result)
    return results


if __name__ == '__main__':
    # 测试
    # prompt = init_history_prompt()
    # print(prompt)

    # 测试
    validation_text = [
        '2025-02-15，寓意吉祥的节日，股票佰笃[BD]美股开盘价10美元，虽然经历了波动，但最终以13美元收盘，成交量微幅增加至460,000，投资者情绪较为平稳。',
        '2025-04-05，市场迎来轻松氛围，股票盘古(0021)开盘价23元，尽管经历了波动，但最终以26美元收盘，成交量缩小至310,000，投资者保持观望态度。',
    ]

    extract_model(validation_text)
