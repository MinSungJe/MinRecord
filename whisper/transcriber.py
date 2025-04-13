import whisper

def transcribe_audio(file_path):
    model = whisper.load_model("turbo")
    result = model.transcribe(file_path)
    return result["text"]