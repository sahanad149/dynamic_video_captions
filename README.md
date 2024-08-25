# Project 1: Video Caption Tool

## Overview
This project automatically adds dynamic captions and animated text overlays to video clips based on AI-generated transcript summaries. It uses TensorFlow for transcript summarization, OpenCV for video processing, and FFMPEG for video encoding.

## File Structure
- **backend/**: Contains the Flask server and video processing scripts.
- **frontend/**: Contains the HTML, CSS, and JavaScript files for the user interface.
- **data/**: Stores example transcript files for testing.

## Setup

### Backend
1. Navigate to the `backend/` directory.
2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the Flask server:
    ```bash
    python app.py
    ```

### Frontend
1. Open the `frontend/index.html` file in a web browser to access the interface.

## Usage
1. Upload a video file through the frontend.
2. The Flask backend will process the video, add captions, and return the final video.
3. The video with captions will be previewed in the frontend.

## Future Enhancements
- Implement additional text animations using `moviepy`.
- Allow users to customize caption styles and animations from the frontend.
