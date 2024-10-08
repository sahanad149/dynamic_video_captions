import os
import cv2
import ffmpeg
import tensorflow as tf
from transformers import T5Tokenizer, T5ForConditionalGeneration

def summarize_transcript(transcript):
    tokenizer = T5Tokenizer.from_pretrained('t5-small')
    model = T5ForConditionalGeneration.from_pretrained('t5-small')
    
    input_ids = tokenizer.encode(transcript, return_tensors="pt", max_length=512, truncation=True)
    summary_ids = model.generate(input_ids, max_length=150, min_length=30, length_penalty=2.0, num_beams=4, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    
    return summary

def add_text_overlay(input_video_path, output_video_path, summary):
    cap = cv2.VideoCapture(input_video_path)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_video_path, fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))
    
    font = cv2.FONT_HERSHEY_SIMPLEX
    text = summary
    position = (50, 50)
    font_scale = 1
    font_color = (255, 255, 255)
    line_type = 2

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        cv2.putText(frame, text, position, font, font_scale, font_color, line_type)
        out.write(frame)

    cap.release()
    out.release()

def encode_video(input_video_path, output_video_path):
    (
        ffmpeg
        .input(input_video_path)
        .output(output_video_path, vcodec='libx264', acodec='aac')
        .run()
    )

def process_video(file_path):
    transcript = "Example transcript"  # Replace with actual transcript extraction logic
    summary = summarize_transcript(transcript)

    # Save transcript summary
    if not os.path.exists('uploads/data'):
        os.makedirs('uploads/data')
    transcript_path = os.path.join('uploads', 'data', 'transcript.txt')
    with open(transcript_path, 'w') as f:
        f.write(summary)

    # Add text overlay and encode video
    output_path = file_path.replace('.mov', '_output.mov')
    add_text_overlay(file_path, output_path, summary)
    
    encoded_output_path = output_path.replace('.mov', '_encoded.mp4')
    encode_video(output_path, encoded_output_path)

    return transcript_path, encoded_output_path
