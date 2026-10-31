from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()


"""
因为 Qwen 本身是模型，而 openai 库是帮你调用模型的工具。两者不必来自同一家公司。
调用远程模型，本质上是发送 HTTP 请求。你需要把问题打包成 JSON、带上密钥、发送请求，再解析返回结果。
openai 库把这些工作封装好了，让已经使用 OpenAI 库的开发者，改一下地址、密钥和模型名，就能调用 Qwen，减少改代码的工作。
这个库的名字叫 openai，看起来像只能调用它自家的模型。实际上，只要服务商支持这种接口格式，它也能调用其他家的模型。
并不是必须用它。 调用百炼，你也可以用：
- OpenAI Python 库：方便在支持兼容接口的服务商之间切换。
- 阿里云 DashScope SDK：使用阿里云自己的调用工具。
- 直接发送 HTTP 请求：自己处理请求和响应。
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
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "你是谁？"},
    ],
)


print(completion.choices[0].message.content)
# sk-ws-H.PXMDHMI.L69T.MEYCIQDmRtdepRun8WG9WDEysvG4g3mNrWmvRTxl3WSi0_5VegIhAKYfLkpFJ1HK6JLPOeb0OW8J3VRZIJKsoTmdaaRE0kPx
