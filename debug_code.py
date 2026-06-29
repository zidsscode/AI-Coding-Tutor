from gemini_helper import ask_gemini

def debug_code():

    print("\nPaste your code (type END on a new line when finished):")

    lines = []

    while True:
        line = input()

        if line.strip().upper() == "END":
            break

        lines.append(line)

    code = "\n".join(lines)

    prompt = f"""
You are a senior Python developer.

Debug the following code.

Return your answer in this format:

❌ What's Wrong

✅ Corrected Code

📖 Explanation for this question in one line:


Code:
{code}
"""

    try:
        answer = ask_gemini(prompt)
        print("\n===== AI RESPONSE =====")
        print(answer)

    except Exception as e:
        print("\n❌ Something went wrong.")
        print(e)