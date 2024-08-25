from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
from process_video import summarize_transcript, add_text_overlay, encode_video

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_video():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"})
    
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join('uploads', filename)
        file.save(filepath)

        # Example: Reading transcript from a file (can be modified to read from an API or other source)
        with open('data/example_transcript.txt', 'r') as f:
            transcript = f.read()

        # Process the video
        summary = summarize_transcript(transcript)
        output_path = os.path.join('uploads', f"output_{filename}")
        add_text_overlay(filepath, output_path, summary)
        encode_video(output_path, output_path)
        
        return jsonify({"output_video": output_path})

if __name__ == "__main__":
    app.run(debug=True)
