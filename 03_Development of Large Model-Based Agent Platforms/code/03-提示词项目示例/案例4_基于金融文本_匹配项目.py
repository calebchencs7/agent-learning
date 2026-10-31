"""
三.文本匹配
1.参考文本
examples = {
    '是': [
        ('公司ABC发布了季度财报，显示盈利增长。', '财报披露，公司ABC利润上升。'),
    ],
    '不是': [
        ('黄金价格下跌，投资者抛售。', '外汇市场交易额创下新高。'),
        ('央行降息，刺激经济增长。', '新能源技术的创新。')
    ]
}


2.验证文本
[
    ('股票市场今日大涨，投资者乐观。', '持续上涨的市场让投资者感到满意。'),
    ('油价大幅下跌，能源公司面临挑战。', '未来智能城市的建设趋势愈发明显。'),
    ('利率上升，影响房地产市场。', '高利率对房地产有一定冲击。'),
]
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
    examples = {
        '相似': [
            ('公司ABC发布了季度财报，显示盈利增长。', '财报披露，公司ABC利润上升。'),
        ],
        '不相似': [
            ('黄金价格下跌，投资者抛售。', '外汇市场交易额创下新高。'),
            ('央行降息，刺激经济增长。', '新能源技术的创新。'),
        ],
    }
    # 准备系统提示词

    system_prompt = f"""你是一个专业的文本匹配模型，你需要根据提供的文本内容，判断两个文本是否表达相同或相似的含义。然后返回相似或者不相似的判断结果"""
    history_prompt = [{'role': 'system', 'content': system_prompt}]

    # 系统提示词拼接小样本
    for label, example_pairs in examples.items():
        for example in example_pairs:
            history_prompt.append(
                {
                    'role': 'user',
                    'content': f"文本1: {example[0]} \n文本2: {example[1]}，是否相似？",
                }
            )
            history_prompt.append({'role': 'assistant', 'content': label})

    # print(history_prompt)
    return history_prompt


# TODO 2.调用模型完成文本匹配（传入验证文本）
client = OpenAI(
    api_key=os.getenv("BAILIAN_API_KEY"),
    base_url="https://ws-9p62epy2octdhspq.cn-beijing.maas.aliyuncs.com/compatible-mode/v1",
)


# 定义API接口
def match_model(texts):
    results = []
    for text in texts:
        completion = client.chat.completions.create(
            # 模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
            model="qwen-plus",
            messages=init_history_prompt()
            + [
                {
                    'role': 'user',
                    'content': f"文本1: {text[0]} \n文本2: {text[1]}，是否相似？",
                }
            ],
        )
        result = completion.choices[0].message.content
        print(f"文本: {text} -> 匹配结果: {result}")
        results.append(result)
    return results


if __name__ == '__main__':
    # 测试
    # prompt = init_history_prompt()
    # print(prompt)

    # 测试
    validation_text = [
        ('股票市场今日大涨，投资者乐观。', '持续上涨的市场让投资者感到满意。'),
        ('油价大幅下跌，能源公司面临挑战。', '未来智能城市的建设趋势愈发明显。'),
        ('利率上升，影响房地产市场。', '高利率对房地产有一定冲击。'),
        ('I love you', 'I miss you'),
    ]

    match_model(validation_text)
