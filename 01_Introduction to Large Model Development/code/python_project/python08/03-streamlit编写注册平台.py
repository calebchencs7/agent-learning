import streamlit as st

# 构建用户注册平台
st.title('用户注册平台')
# 分隔线
st.divider()
# information
name = st.text_input('请输入您的姓名:')
pwd = st.text_input('请输入您的密码:', type='password')
age = st.number_input('请输入您的年龄:', min_value=1, max_value=100, step=1)
email = st.text_input('请输入您的邮箱:')
gender = st.radio('请输入您的性别:', options=['男', '女', '保密'], horizontal=True)
birthday = st.date_input('请输入您的生日:')
height = st.slider('请输入您的身高:', min_value=0, max_value=300, step=1)
result = st.button('注册')
if result:
    st.write("录入成功！")
    with open("users.txt", "a", encoding='utf-8') as f:
        f.write(f'姓名:{name},密码:{pwd},年龄:{age},邮箱:{email},性别:{gender},生日:{birthday},身高:{height}\n')
else:
    st.write('请填写完整信息后点击注册按钮')
