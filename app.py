import streamlit as st
from gemini_helper import ask_gemini

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Coding Tutor",
    page_icon="🤖",
    layout="wide"
)

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.title("🤖 AI Coding Tutor")
    st.markdown("---")

    st.subheader("👨‍💻 Developer")
    st.write("**Zidaan Shaikh**")

    st.markdown("---")

    st.subheader("📚 Features")

    st.markdown("""
- Explain Code
- Debug Code
- Python Questions
- Theory Questions
- Gemini AI Powered
""")

    st.markdown("---")
    st.success("AI & ML Diploma Project")

# ---------------- HEADER ----------------
st.title("🤖 AI Coding Tutor")

st.markdown("""
### Learn Python with the help of Gemini AI

Paste your Python code or ask any programming question.
""")

st.markdown("---")

# ---------------- OPTION ----------------
option = st.selectbox(
    "Choose Task",
    [
        "Explain Code",
        "Debug Code",
        "Python Coding Question",
        "Theory Question"
    ]
)

# ---------------- INPUT ----------------
user_input = st.text_area(
    "Enter your code or question",
    height=200,
    placeholder="Paste Python code or type your question here..."
)

col1, col2 = st.columns(2)

submit = col1.button("🚀 Generate Answer", use_container_width=True)
clear = col2.button("🗑 Clear", use_container_width=True)

if clear:
    st.rerun()

# ---------------- PROMPTS ----------------
if submit:

    if user_input.strip() == "":
        st.warning("Please enter some text.")
        st.stop()

    if option == "Explain Code":
        prompt = f"Explain this Python code in simple language in short:\n\n{user_input}"

    elif option == "Debug Code":
        prompt = f"Find errors in this Python code and provide the corrected version:\n\n{user_input}"

    elif option == "Python Coding Question":
        prompt = f"Solve this Python coding question with short explanation:\n\n{user_input}"

    else:
        prompt = f"Answer this Python theory question in points:\n\n{user_input}"

    with st.spinner("🤖zid's AI is thinking... "):
        answer = ask_gemini(prompt)

    st.markdown("---")
    st.subheader("✅ zid's AI Response")

    st.success(answer)

# ---------------- FOOTER ----------------
st.markdown("---")

st.markdown(
    """
<div style='text-align:center; color:gray;'>

Made with ❤️ using Streamlit + Google Gemini

**Developer:** Zidaan Shaikh

</div>
""",
unsafe_allow_html=True,
)