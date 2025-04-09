import whisper

def get_text_from_record():
    model = whisper.load_model("turbo")
    result = model.transcribe("record\\record.m4a")
    return result["text"]

if __name__ == "__main__":
    get_text_from_record()