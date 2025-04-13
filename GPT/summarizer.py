import os
from openai import OpenAI

def summarize_text(text, instructions_path="instructions.md"):
    try:
        with open(instructions_path, "r", encoding="utf-8") as file:
            instructions = file.read()
    except FileNotFoundError:
        print(f"Instruction file '{instructions_path}' not found.")
        return None

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": instructions},
            {"role": "user", "content": text}
        ],
    )
    return response.choices[0].message.content