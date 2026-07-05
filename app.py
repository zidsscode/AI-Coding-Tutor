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
✅ Explain Code

✅ Debug Code

✅ Coding Questions

✅ Theory Questions
""")

    st.markdown("---")

    st.subheader("🛠 Tech Stack")

    st.markdown("""
🐍 Python

🌐 Streamlit

🤖 Google Gemini
""")

    st.markdown("---")

    st.success("Version 1.0")

# ---------------- HERO HEADER ----------------

st.markdown("""
<div style="
background: linear-gradient(90deg,#2563eb,#7c3aed);
padding:30px;
border-radius:18px;
text-align:center;
color:white;
">

<h1>🤖 AI Coding Tutor</h1>

<h3>Learn Python Smarter with Zid'AI</h3>

<p style="font-size:18px;">
💡 Explain Code &nbsp;&nbsp;|&nbsp;&nbsp;
🐞 Debug Code &nbsp;&nbsp;|&nbsp;&nbsp;
📖 Theory Questions &nbsp;&nbsp;|&nbsp;&nbsp;
💻 Coding Questions
</p>

<p><b>Developed by Zidaan Shaikh</b></p>

</div>
""", unsafe_allow_html=True)

st.write("")

# ---------------- FEATURE CARDS ----------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.info("💻\n\nCoding Questions")

with col2:
    st.success("📖\n\nExplain Code")

with col3:
    st.warning("🐞\n\nDebug Code")

with col4:
    st.error("🧠\n\nTheory Questions")

st.write("")

# ---------------- TASK ----------------

option = st.selectbox(
    "📌 Choose Your Task",
    (
        "Explain Code",
        "Debug Code",
        "Python Coding Question",
        "Theory Question"
    )
)

# ---------------- INPUT ----------------

user_input = st.text_area(
    "✍ Enter your code or question",
    height=220,
    placeholder="Paste your Python code or type your question here..."
)

st.write("")

col1, col2 = st.columns(2)

submit = col1.button("🚀 Generate Answer", use_container_width=True)
clear = col2.button("🗑 Clear", use_container_width=True)

if clear:
    st.rerun()

# ---------------- AI ----------------

if submit:

    if user_input.strip() == "":
        st.warning("⚠ Please enter your code or question.")
        st.stop()

    if option == "Explain Code":
        prompt = f"""
Explain this Python code in simple language.

Keep the explanation beginner-friendly.

Code:

{user_input}
"""

    elif option == "Debug Code":
        prompt = f"""
You are a Python debugging expert.

Find all errors.

Explain why they occur.

Provide corrected code.

Code:

{user_input}
"""

    elif option == "Python Coding Question":
        prompt = f"""
Solve this Python question.

Explain the logic briefly.

Question:

{user_input}
"""

    else:
        prompt = f"""
Explain this Python theory topic.

Answer in easy points.

Question:

{user_input}
"""

    with st.spinner("🤖 Zid'AI is thinking..."):

        answer = ask_gemini(prompt)

    st.write("")

    st.subheader("🤖 Zid'AI Response")

    st.markdown(answer)

# ---------------- FOOTER ----------------

st.markdown("---")

st.markdown(
"""
<div style="text-align:center;color:gray;">

Made with ❤️ using Python • Streamlit • Google Gemini

<br>

<b>Developed by Zidaan Shaikh</b>

</div>
""",
unsafe_allow_html=True
)