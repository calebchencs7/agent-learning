from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

SYSTEM_PROMPT = """
你是一个帮助用户判断段谁最高的人，请你用COT的方法进行推理。
你需要一步步思考，步骤如下：
问题：
张三比李四跑的快，李四比王五跑的快，那么谁跑的最快？
答案：张三比李四跑的快，李四比王五跑的快，
     张三>李四，李四>王五，所以张三>王五
     推断张三跑的最快
     张三最快
"""


client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com",
)

response = client.chat.completions.create(
    model="deepseek-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "A比B高，C比A高，那么谁最高？"},
    ],
    max_tokens=1024,
    temperature=0.7,
    stream=False,
)

print(response.choices[0].message.content)
