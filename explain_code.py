from gemini_helper import ask_gemini

def explain_code():

    print("\nPaste your code (type END on a new line when finished):")

    lines = []

    while True:
        line = input()

        if line.strip().upper() == "END":
            break

        lines.append(line)

    code = "\n".join(lines)

    prompt = f"""
You are an expert Python teacher.

Explain the following code.

Your response must include:

1. Purpose of the code
2. Line-by-line explanation in short
3. Expected Output
4. Time Complexity


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