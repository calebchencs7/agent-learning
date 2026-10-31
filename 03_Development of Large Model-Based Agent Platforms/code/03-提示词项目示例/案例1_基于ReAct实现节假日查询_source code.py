"""
练习
"""

"""
核心思路：
1.先准备调用模型的API接口(call_llm)
2.准备模型需要的工具(get_current_month, get_holidays)
3.开始编写ReAct的功能(思考->行动->观察->思考->行动->观察->...->最终回答符合用户问题的答案)
"""


# 导包
from openai import OpenAI
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()


# TODO: 1.先准备调用模型的API接口(call_llm)
# 创建模型客户端
client = OpenAI(
    api_key=os.getenv("BAILIAN_API_KEY"),
    base_url="https://ws-9p62epy2octdhspq.cn-beijing.maas.aliyuncs.com/compatible-mode/v1",
)


def call_llm(prompt, model="qwen-plus"):
    """
    调用模型的API接口
    :param prompt: 模型的提示词
    :param model: 模型名称
    :return: 模型的输出结果
    """
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "你是一个智能助手。"},
            {"role": "user", "content": prompt},
        ],
    )
    return completion.choices[0].message.content


# TODO 2.准备模型需要的工具(get_current_month, get_holidays)


def get_current_month():
    return datetime.now().month


def get_holidays(month):
    holidays = {
        "2026年1月": ["元旦: 1月1日-3日"],
        "2026年2月": ["春节: 2月15日-23日"],
        "2026年3月": [],
        "2026年4月": ["清明节: 4月4日-6日"],
        "2026年5月": ["劳动节: 5月1日-5日"],
        "2026年6月": ["端午节: 6月19日-21日"],
        "2026年7月": [],
        "2026年8月": [],
        "2026年9月": ["中秋节: 9月25日-27日"],
        "2026年10月": ["国庆节: 10月1日-7日"],
        "2026年11月": [],
        "2026年12月": [],
    }
    # 根据传入的月份获取对应节假日列表
    month_holidays = holidays.get(f"2026年{month}月", [])
    return month_holidays


# TODO 3.开始编写ReAct的功能(思考->行动->观察->思考->行动->观察->...->最终回答符合用户问题的答案)


# 解析模型返回结果
def parse_model_response(response):
    # 解析模型返回的结果
    thought, action, action_input = response.split("\n")

    thought = thought.replace("Thought:", "").strip()
    action = action.replace("Action:", "").strip()
    action_input = action_input.replace("Action Input:", "").strip()

    print("模型思考:", thought)
    print("模型行动:", action)
    print("模型行动输入:", action_input)

    return thought, action, action_input


def model_react_pattern(prompt):
    print("用户问题:", prompt)
    user_question = prompt  # 保留原始问题，避免下一轮把整段提示词当成问题
    # 提前定义一个列表，存储模型每一步的结果
    steps = []

    print("开启ReAct流程...")
    for i in range(3):  # 限制模型最多思考3次
        context = '\n'.join(steps)  # 上下文信息
        react_prompt = f"""
            你是一个专业的ReAct智能代理,接下来用户问你问题,你需要严格的按照以下格式返回结果,不允许添加额外无关内容!!!!
                Thought: <此处放你的思考内容>
                Action: <只能是 get_current_month、get_holidays 或 Final Answer>
                Action Input: <get_current_month 填 {{}}；get_holidays 填月份数字；Final Answer 填最终答案>
            如果上下文中还没有月份，调用 get_current_month。
            如果已有月份但还没有节假日查询结果，调用 get_holidays。
            如果已有 get_holidays 的 Observation，下一步必须使用 Final Answer 回答用户，不再调用工具。
            上下文:{context}
            用户问题:
                {user_question}
            """
        # 调用模型
        response = call_llm(react_prompt)

        # 解析模型返回结果
        thought, action, action_input = parse_model_response(response)
        # 把结果添加到步骤列表中去
        steps.append(f"Thought: {thought}")
        steps.append(f"Action: {action}")
        steps.append(f"Action Input: {action_input}")

        # print(steps)

        # 调用工具获取当前月
        if action == "get_current_month":
            current_month = get_current_month()
            steps.append(f"Observation: {current_month}")
            print("模型观察上一步结果:", current_month)
        elif action == "get_holidays":
            holidays = get_holidays(current_month)
            steps.append(f"Observation: {holidays}")
            print("模型观察上一步结果:", holidays)
        elif action == "Final Answer":
            print("模型最终回答:", action_input)
            break


if __name__ == "__main__":
    # # 测试调用模型的API接口
    # prompt = "请告诉我1+1等于几"
    # result = call_llm(prompt)
    # print(result)

    # # 测试获取当前月份
    # current_month = get_current_month()
    # print(f"当前月份是：{current_month}")

    # # 测试获取到节假日
    # holidays = get_holidays(current_month)
    # print(f"{current_month}月的节假日有：{holidays}")

    # TODO 调用ReAct
    model_react_pattern("查询本月有哪些节假日?")
