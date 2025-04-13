from dotenv import load_dotenv
from Whisper.transcriber import transcribe_audio
from GPT.summarizer import summarize_text

load_dotenv()

if __name__ == "__main__":
    # 음성 파일 경로
    audio_file_path = "record/record.m4a"

    # 1. 음성 파일 텍스트 변환
    print("Transcribing audio...")
    transcribed_text = transcribe_audio(audio_file_path)
    print("Transcription complete.")

    # 2. 텍스트 요약
    print("Summarizing text...")
    summary = summarize_text(transcribed_text)
    print("Summary complete.")

    # 3. 결과 출력
    print("\n--- Transcribed Text ---")
    print(transcribed_text)
    print("\n--- Summary ---")
    print(summary)