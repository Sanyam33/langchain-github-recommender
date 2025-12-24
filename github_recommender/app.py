import streamlit as st
from agent import agent


st.title("Find Open Source Projects")
st.subheader("OSS Project suggestion that matches your interests")

username = st.text_input("Github Username", placeholder='Enter Github username')
get_projects = st.button('Find Projects',type="primary")


# def stream_generator():
#     for chunk, metadata in agent.stream({"messages": [{'role':'user','content':username}]}, stream_mode="messages"):
#         yield chunk.content

if username and get_projects:
    with st.chat_message("assistant"):
        response = agent.invoke({"messages": [{'role':'user','content':username}]})
        st.write(response['messages'][-1].content)