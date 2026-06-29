from gemini_helper import ask_gemini

def coding_question():
    question = input("\nAsk your coding question: ").strip()

    if not question:
        print("\n❌ Question cannot be empty.")
        return
    prompt = f"""
You are an AI Coding Tutor.

Instructions:
- Answer coding questions clearly.
-  provide Python code first.
- If the user asks for explanation, answer the question.


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