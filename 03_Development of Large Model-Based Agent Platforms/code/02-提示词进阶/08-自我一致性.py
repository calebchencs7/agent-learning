"""
需求：Self-Consistency通过结合Prompt Chaining，实现问题的拆解、执行和投票
思路步骤：
0.
1. 生成不同思路：3个
2. 将每个思路拼接成一个prompt，分别调用大模型得到结果
3. 每个思路的结果进行投票
"""

import json
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("BAILIAN_API_KEY"),
    base_url="https://ws-9p62epy2octdhspq.cn-beijing.maas.aliyuncs.com/compatible-mode/v1",
)


# 0.调用Qwen模型
def call_llm(prompt):
    response = client.chat.completions.create(
        model="qwen3.8-flash",
        messages=[{'role': 'user', 'content': prompt}],
    )
    if not response.choices or response.choices[0].message.content is None:
        raise RuntimeError("模型调用成功，但没有返回文本内容")
    return response.choices[0].message.content


# 1. 生成不同思路：3个
question = """
            一个商店卖铅笔，每支2元。如果小明有20元，他最多能买多少支铅笔？
            """

step1_prompt = f"""
                你是一个数学老师。请用3种不同的方法来推理这个问题，只需给出推理思路，不需要解答。思路需要简洁明了，并且合理有效。
                输出格式为：["思路1：...","思路2：...","思路3：..."]
                问题如下：
                {question}
                """
# call_llm调用后的的输出格式为：思路1：...，思路2：...，思路3：...这样的的字符串，但是内容像json

solution_list = call_llm(step1_prompt)
print(f'step1_result->{solution_list}')

# 2.循环遍历每个思路
step2_result_list = []
for solution in json.loads(solution_list):  # 把 JSON 字符串转换成 Python 列表
    # 将每个思路拼接成一个prompt，分别调用大模型得到结果
    step2_prompt = f"""
                    你是一个数学老师。请用如下的思路来解决这个问题。只输出答案即可。
                    思路：
                    {solution}
                    问题：
                    {question}"""
    step2_result = call_llm(step2_prompt)
    step2_result_list.append(step2_result)
print(f'step2_result_list->{step2_result_list}')

# 3. 每个思路的结果进行投票
step3_prompt = f"""
                你是一个公正的投票专家，能够根据用户输入的list格式的多个答案进行投票，哪个答案出现的次数最多
                你就返回哪个答案，需要注意，返回的答案只需要有计算结果就行，不要有过程。
                用户输入的多个答案：
                {step2_result_list}
                """

step3_result = call_llm(step3_prompt)

print(f'step3_result->{step3_result}')
