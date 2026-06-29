from gemini_helper import ask_gemini

def theory_question():
    question = input("\nAsk your theory question: ").strip()

    if not question:
        print("\n❌ Question cannot be empty.")
        return

    prompt = f"""
You are a Python programming teacher.

Explain this topic using this format:

Definition in two lines:

Example in one line:


Question:
{question}
"""

    try:
        answer = ask_gemini(prompt)
        print("\n===== AI RESPONSE =====")
        print(answer)

    except Exception as e:
        print("\n❌ Something went wrong.")
        print(e)