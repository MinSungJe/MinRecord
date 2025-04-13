import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
instructions_path = "instructions.md"
instructions = None

text = '여기에 텍스트 내용이 들어갑니다.'  # 예시 텍스트

# 지침 파일 읽기
def load_instructions(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Instruction file '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred while reading the instruction file: {e}")
        return None

# 지침 파일 읽어오기
def initialize_instructions():
    global instructions
    instructions = load_instructions(instructions_path)
    if not instructions:
        print("Failed to load instructions. The application might not work as expected.")

# 요약
def get_summary_by_gpt(text: str):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": instructions},
            {"role": "user", "content": f"{text}"}
        ],
    )
    summary = response.choices[0].message.content
    return summary


if __name__ == "__main__":
    initialize_instructions()
    summary = get_summary_by_gpt(text)
    print(summary)