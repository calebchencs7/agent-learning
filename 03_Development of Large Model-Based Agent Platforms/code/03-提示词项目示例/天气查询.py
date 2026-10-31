# 工具函数
from datetime import datetime, timedelta
from http import HTTPStatus
import os
import dashscope

import dotenv

dotenv.load_dotenv()

dashscope.api_key = os.getenv("BAILIAN_API_KEY") or os.getenv("DASHSCOPE_API_KEY")


def get_tomorrow_date():
    # 获取明日标准日期字符串
    tomorrow = datetime.now() + timedelta(days=1)
    return tomorrow.strftime("%Y-%m-%d")


# 模拟天气数据库
weather_db = {
    ("北京", "2026-10-30"): {"weather": "小雨", "temp": "18~24℃", "rain_prob": "80%"}
}


def get_weather(city, date):
    """根据城市+日期查询天气，无数据返回提示文本"""
    return weather_db.get((city, date), "未查询到该城市对应日期的天气信息")


# 工具注册字典
TOOLS = {"get_tomorrow_date": get_tomorrow_date, "get_weather": get_weather}


# 调用大模型生成ReAct思考/行动文本
def call_LLM(prompt):
    if not dashscope.api_key:
        raise RuntimeError(
            "请在环境变量或 .env 文件中设置 BAILIAN_API_KEY 或 DASHSCOPE_API_KEY。"
        )
    response = dashscope.Generation.call(
        model='qwen-plus',
        messages=[{'role': 'user', 'content': prompt}],
    )
    if response.status_code != HTTPStatus.OK:
        raise RuntimeError(
            f"大模型调用失败（HTTP {response.status_code}，"
            f"错误码 {response.code}）：{response.message}"
        )
    if response.output is None or not response.output.text:
        raise RuntimeError("大模型调用成功，但返回内容为空。")
    return response.output.text


def parse_model_output(output):
    """
    解析模型输出，提取 Thought, Action, Action Input
    不使用正则表达式，使用简单的字符串处理
    """
    thought = ""
    action = ""
    action_input = ""

    lines = output.split('\n')

    for line in lines:
        line = line.strip()
        if line.startswith('Thought:'):
            thought = line.replace('Thought:', '').strip()
        elif line.startswith('Action:'):
            action = line.replace('Action:', '').strip()
        elif line.startswith('Action Input:'):
            action_input = line.replace('Action Input:', '').strip()

    return thought, action, action_input


# ==================请按题目要求补全此处代码================
# 核心ReAct循环函数，需自行完成循环、工具调用、观测回传、终止判断逻辑
def react_solve(question):
    import json

    max_steps = 8
    weather_observed = False

    needs_tomorrow = "明天" in question
    tomorrow_date = None

    prompt = f"""你是一个天气出行助手，请通过工具查询后回答用户问题。

                可用工具：
                1. get_tomorrow_date：获取明天的日期，不需要参数。
                2. get_weather：查询指定城市和日期的天气。
                参数：city（城市）、date（YYYY-MM-DD 格式日期）。

                规则：
                - 每次只调用一个工具，并严格使用以下格式：
                Thought: 简要说明下一步
                Action: 工具名称
                Action Input: 单行 JSON 对象
                - get_tomorrow_date 的 Action Input 必须为 {{}}。
                - get_weather 的 Action Input 示例：
                {{"city": "北京", "date": "2026-06-17"}}
                - 如果用户询问明天的天气，先调用 get_tomorrow_date，
                再使用返回的日期调用 get_weather。
                - 天气信息必须来自 get_weather 的 Observation，不能自行编造。
                - 查询不到天气时，如实说明无法查询，不要猜测天气。
                - 完成工具调用后，只使用以下格式输出最终回答：
                Answer: 你的回答

                用户问题：{question}
            """

    for _ in range(max_steps):
        # 调用模型，并将本轮输出加入上下文
        output = call_LLM(prompt)
        prompt += f"\n{output}\n"

        # 最终回答分支
        answer_lines = [
            line.strip()
            for line in output.splitlines()
            if line.strip().startswith("Answer:")
        ]

        if answer_lines:
            answer = answer_lines[0].split("Answer:", 1)[1].strip()

            # 天气问题必须先执行天气查询，防止跳过工具直接作答
            if not weather_observed:
                prompt += (
                    "Observation: 你还没有调用天气查询工具，"
                    "不能直接回答。请先调用所需工具。\n"
                )
                continue

            return answer or "模型未提供有效回答。"

        # 工具调用分支
        thought, action, action_input = parse_model_output(output)

        if not thought or not action or not action_input:
            observation = (
                "输出格式不完整。请包含 Thought:、Action: "
                "和 Action Input:，或者在完成查询后输出 Answer:。"
            )
        elif action not in TOOLS:
            observation = f"工具不存在：{action}，请从已注册工具中选择。"
        else:
            try:
                params = json.loads(action_input)

                if not isinstance(params, dict):
                    raise ValueError("Action Input 必须是 JSON 对象。")

                if action == "get_tomorrow_date":
                    if params:
                        raise ValueError("get_tomorrow_date 不需要参数，请传入 {}。")

                    result = TOOLS[action]()
                    tomorrow_date = result
                    observation = result

                elif action == "get_weather":
                    if set(params) != {"city", "date"}:
                        raise ValueError("get_weather 需要 city 和 date 两个参数。")

                    if needs_tomorrow and tomorrow_date is None:
                        raise ValueError("请先调用 get_tomorrow_date 获取明天的日期。")

                    if needs_tomorrow and params["date"] != tomorrow_date:
                        raise ValueError(
                            "查询日期必须与 get_tomorrow_date 的结果一致。"
                        )

                    result = TOOLS[action](**params)
                    weather_observed = True

                    # 无数据也作为观察结果返回，要求模型如实说明
                    observation = json.dumps(result, ensure_ascii=False)

            except (json.JSONDecodeError, TypeError, ValueError) as exc:
                observation = f"工具参数错误：{exc}"

        # 将工具结果或错误信息加入上下文，供下一轮模型使用
        prompt += f"Observation: {observation}\n"

    return "达到最大执行步数，未能完成天气查询和出行建议。"


# =======================================================

# 程序入口测试
if __name__ == "__main__":
    question = "我明天去北京出差，需要带雨伞吗？"
    final_answer = react_solve(question)
    print("最终出行建议：", final_answer)
