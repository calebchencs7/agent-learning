import streamlit as st
from chat_utils.ollama_chat_result import get_ollama_response

st.title('ChatBox界面')

st.divider()

# TODO 判断消息列表是否在session_state字典中，如果不在就创建一个
if 'messages' not in st.session_state:
    st.session_state.messages = [
        {'role': 'assistant', 'content': "Hi there! I'm your AI assistant. How can I help you today?"}
    ]

# 创建一个聊天框
# 1. ai开场白
for message in st.session_state["messages"]:
    st.chat_message(message['role']).write(message['content'])

# 2. 用户输入提示词
prompt = st.chat_input("Type your message here...")

if prompt:
    # 3. 显示用户输入
    st.chat_message('user').write(prompt)
    # 将用户的输入添加到消息列表中
    st.session_state['messages'].append({'role': 'user', 'content': prompt})

    # 4. AI根据用户的提示词，调用大模型回复答案
    with st.spinner("AI is thinking..."):
        # 调用ollama模型获取AI回复
        response = get_ollama_response(st.session_state['messages'])
    # 5. 显示AI的回复
    st.chat_message('assistant').write(response)
    # 将AI的回复添加到消息列表中
    st.session_state['messages'].append({'role': 'assistant', 'content': response})
