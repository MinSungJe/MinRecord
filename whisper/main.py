import whisper

model = whisper.load_model("turbo")
result = model.transcribe("record\\record.m4a")
print(result["text"])