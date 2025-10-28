import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import streamlit as st
from components import show_header, show_footer, navigate_to_page,back_to_dashboard_button


st.set_page_config(page_title="Health Prediction", page_icon="🧬")
show_header()


st.markdown("### 🩺 Health Risk Prediction")


# TODO: Add model integration here later
st.text_input("Enter your age:")
st.text_input("Enter your BP:")
st.text_input("Enter your heart rate:")


if st.button("Predict Health Risk"):
    st.success("⚠️ Prediction: [Sample Output]. Please consult a doctor.")


if st.button("Consult Doctor / Chatbot"):
    navigate_to_page("pages/medical_bot.py")

back_to_dashboard_button()
show_footer()