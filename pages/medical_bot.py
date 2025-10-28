import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import streamlit as st
import requests
from components import show_header, show_footer,back_to_dashboard_button


st.set_page_config(page_title="Medical Chatbot", page_icon="🤖")
show_header()


st.markdown("### 💬 Medical AI Assistant")


if 'chat_history' not in st.session_state:
   st.session_state.chat_history = []


user_input = st.text_input("You:")


if st.button("Send") and user_input:
# Simulated local API call
    response = requests.post("http://127.0.0.1:8000/chat", json={"message": user_input})
    bot_reply = response.json().get("response", "Sorry, no reply.")


    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", bot_reply))


for role, msg in st.session_state.chat_history:
   st.chat_message(role.lower()).markdown(msg)

back_to_dashboard_button()
show_footer()