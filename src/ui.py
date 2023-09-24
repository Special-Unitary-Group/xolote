import streamlit as st

from llm import reply

st.title("Kanban")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hi! Ask me anything about the papers you have provided.",
        }
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask about your papers!"):
    st.chat_message("user").markdown(prompt)

    st.session_state.messages.append({"role": "user", "content": prompt})

    response = reply("default", prompt)

    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})
