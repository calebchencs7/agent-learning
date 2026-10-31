import dashscope
import os
from dotenv import load_dotenv

load_dotenv()

dashscope.base_http_api_url = (
    "https://ws-9p62epy2octdhspq.cn-beijing.maas.aliyuncs.com/api/v1"
)

messages = [
    {'role': 'system', 'content': [{'text': 'You are a helpful assistant.'}]},
    {'role': 'user', 'content': [{'text': '你是谁？'}]},
]
response = dashscope.MultiModalConversation.call(
    api_key=os.getenv("BAILIAN_API_KEY"),
    model="qwen3.8-flash",
    messages=messages,
)
print(response.output.choices[0].message.content[0]["text"])
