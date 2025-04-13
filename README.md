# ⏺️ MinRecord

녹음된 음성 파일을 쉽게 요약하세요!

## 🤔 목표

- whisper 모듈과 OpenAI API를 이용해 음성 파일을 쉽게 요약하는 서비스 제작

### 사용 기술 스택

![ChatGPT](https://img.shields.io/badge/chatGPT-74aa9c?style=for-the-badge&logo=openai&logoColor=white) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)

## ⛳ 구현할 기능 목록

### 구현

- [x] whisper 모듈을 이용해 음성 파일을 글로 변환한다.
- [x] OpenAI API를 이용해 녹음 내용을 요약한다.
  - 지침서를 따로 만들어 원하는 프롬프트를 적용한다.

### 서버 구축

- [x] Flask를 이용해 서버로 구축한다.

### 서비스 제작

- [ ] 간단한 웹 페이지 화면을 만든다.
  - 웹 페이지 내에서 녹음을 할 수 있다.
  - 요약하고 싶은 글을 직접 입력할 수 있다.
- [ ] 만든 웹 페이지에 구현한 기능을 연결한다.
