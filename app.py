import streamlit as st
from gemini_helper import ask_gemini

st.set_page_config(page_title="AI Coding Tutor", page_icon="🤖")

st.title("🤖 AI Coding Tutor")
st.write("Ask coding questions, get explanations, debugging help, and theory answers.")

menu = st.sidebar.selectbox(
    "Choose Feature",
    [
        "Ask Coding Question",
        "Explain Code",
        "Debug Code",
        "Theory Question"
    ]
)

# 1. Ask Coding Question
if menu == "Ask Coding Question":
    question = st.text_input("Enter your coding question")

    if st.button("Get Answer"):
        if question:
            prompt = f"""
You are an expert AI Coding Tutor.
provide code for this question, and give short explanation:.

Question:
{question}
"""
            response = ask_gemini(prompt)
            st.success(response)
        else:
            st.warning("Please enter a question")

# 2. Explain Code
elif menu == "Explain Code":
    code = st.text_area("Paste your code here")

    if st.button("Explain"):
        if code:
            prompt = f"""
Explain this Python code in simple terms and in short:

{code}
"""
            response = ask_gemini(prompt)
            st.success(response)
        else:
            st.warning("Please paste code")

# 3. Debug Code
elif menu == "Debug Code":
    code = st.text_area("Paste buggy code")

    if st.button("Debug"):
        if code:
            prompt = f"""
You are a Python debugging expert.

Find errors and fix the code:

{code}
"""
            response = ask_gemini(prompt)
            st.success(response)
        else:
            st.warning("Please paste code")

# 4. Theory Question
elif menu == "Theory Question":
    question = st.text_input("Ask theory question")

    if st.button("Explain"):
        if question:
            prompt = f"""
Explain this Python concept simply in short:

{question}
"""
            response = ask_gemini(prompt)
            st.success(response)
        else:
            st.warning("Please enter a question")