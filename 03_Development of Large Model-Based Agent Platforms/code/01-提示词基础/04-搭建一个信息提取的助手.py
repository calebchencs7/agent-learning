import os

from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

USER_PROMPT = """
李婉婷
151-9876-5432
北京市海淀区中关村大街1号海龙大厦8层805室
东西是一份文件，已经封装好了。寄普通快递就行，麻烦寄出后把单号发我一下，谢谢啦！
"""


def get_json_data(question):
    # TODO 提前撰写系统提示词
    SYSTEM_PROMPT = """
    你是一个快递信息提取专家，能够根据用户输入的快递地址、人名、手机号信息把对应的实体抽取出来，并以JSON格式返回。比如输入：张明远，138-1234-5678
    广东省深圳市南山区科技园南区高新南一道1000号腾讯大厦18层 1806室，你返回：
    {
    "name": "张明远",
    "phone": "138-1234-5678",
    "address": "广东省深圳市南山区科技园南区高新南一道1000号腾讯大厦18层 1806室"
    }

    需要注意，对于用户的输入，你只返回上述的json格式，不要返回任何其他内容。
    """

    # 创建客户端对象

    client = OpenAI(
        api_key=os.getenv("BAILIAN_API_KEY"),
        base_url="https://ws-9p62epy2octdhspq.cn-beijing.maas.aliyuncs.com/compatible-mode/v1",
    )

    completion = client.chat.completions.create(
        # 模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
        model="qwen3.8-flash",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": USER_PROMPT},
        ],
    )

    return completion.choices[0].message.content


if __name__ == "__main__":
    question = USER_PROMPT
    json_data = get_json_data(question)
    print(json_data)
