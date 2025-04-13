from flask import Flask, request, jsonify
from dotenv import load_dotenv
from Whisper.transcriber import transcribe_audio
from GPT.summarizer import summarize_text

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Endpoint: /request
@app.route('/request', methods=['POST'])
def handle_request():
    audio_file_path = "record/record.m4a"
    
    # Step 1: Transcribe audio
    try:
        transcribed_text = transcribe_audio(audio_file_path)
    except Exception as e:
        return jsonify({"error": f"Failed to transcribe audio: {str(e)}"}), 500

    # Step 2: Summarize text
    try:
        summary = summarize_text(transcribed_text)
    except Exception as e:
        return jsonify({"error": f"Failed to summarize text: {str(e)}"}), 500

    return jsonify({
        "transcribed_text": transcribed_text,
        "summary": summary
    })

# Endpoint: /transcribe
@app.route('/transcribe', methods=['POST'])
def handle_transcribe():
    audio_file_path = "record/record.m4a"
    
    # Transcribe audio
    try:
        transcribed_text = transcribe_audio(audio_file_path)
    except Exception as e:
        return jsonify({"error": f"Failed to transcribe audio: {str(e)}"}), 500

    return jsonify({"transcribed_text": transcribed_text})

# Endpoint: /summarize
@app.route('/summarize', methods=['POST'])
def handle_summarize():
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error": "Missing 'text' in request body"}), 400

    text = data["text"]

    # Summarize text
    try:
        summary = summarize_text(text)
    except Exception as e:
        return jsonify({"error": f"Failed to summarize text: {str(e)}"}), 500

    return jsonify({"summary": summary})

if __name__ == "__main__":
    app.run(debug=True)