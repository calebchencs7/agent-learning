import streamlit as st

st.title('ChatBox界面')

st.divider()

# 创建一个聊天框
# 1. ai开场白
st.chat_message('assistant').write("Hi there! I'm your AI assistant. How can I help you today?")

# 2. 用户输入
prompt = st.chat_input("Type your message here...")

if prompt:
    # 3. 显示用户输入
    st.chat_message('user').write(prompt)
    # 4. AI根据用户的提示词，调用大模型回复答案
