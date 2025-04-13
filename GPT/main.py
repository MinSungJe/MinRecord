import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
instructions_path = "instructions.md"
instructions = None

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
    summary = get_summary_by_gpt("어제 오늘 해서 계속 사우나를 갔다 왔는데요 사우나를 가면서 사우나라는 곳이 어떤 역할을 하고 있는가 그러니까 크게 어떤 걸  하기 위해서 만들어진 공간인가라는 생각을 좀 해보았어요 처음에는 그 기능을 잘 모르겠어서 사우나가 가지고 있는 개별 시설들의 기능을 살펴봤는데 일단 온탕이 있을 거고 그리고 냉탕이 있을 거고 그 다음에 습식사우나, 건식사우나 이렇게 네 가지로 분류를 나눠볼 수 있더라고요 온탕 같은 경우에는 몸을 따뜻하게 해줘가지고 몸의 신진대사라든가 혈액순환을 빠르게 해주는 역할이 있는 것 같아요 특히 이 온탕을 수증기 형식으로 만든 것이 바로 습식사우나 같은 느낌이었고요 습식사우나에서는 땀이 줄줄 나오면서 몸 속에 노폐물도 같이 빼주는 역할도 할 수 있더라고요 건식사우나의 경우에는 습식사우나와 다르게 수증기가 아니라 그냥 더 데핀 공기를 가지고 몸을 따뜻하게 하는 역할인데 이 역할의 경우에는 역시 땀을 빼주는 역할 뿐만 아니라 땀을 빼주는 기능 뿐만 아니라 제 생각에는 신진대사를 하는 기능이 좀 더 많이 부각이 되는 것 같아요 마지막으로 냉탕의 경우에 있는 몸을 깜짝 놀라게 해줌으로써 몸에 긴장감을 더 붙여주는 기능을 했습니다 이 네 가지 기능이 모여서 어떤 역할을 할까라고 생각을 하면은 우리 몸을 몸에 적당한 자극을 주므로써 신진대사를 화발하게 하고 노폐물을 뺄 수 있게끔 해서 우리 몸을 더 건강하게 하는 역할을 하는 곳이다 라는 결 론을 내렸고요 뿐만 아니라 몰입의 조건에도 적당한 난이도가 적당하지만 어려운 난이도가 집중이 되잖아요 이것처럼 우리 몸에게  주는 몰입이다 라고 생각이 드는게 원래 우리 몸은 평소의 공간뿐만 아니라 덥고 춥고 이런 평소의 공간이 아닌 다른 공간을 제공해 줌으로써 우리 몸에게도 몰입할 수 있는 공간을 제공한다 라는 부분도 무시할 수가 없더라고요 결론적으로는 우리 몸이 더욱더 건 강하게 해주는 역할 하에 여러 가지 수술들이 있는 공간이다 라는 것을 알 수 있었습니다 감사합니다")
    print(summary)
