# Visatra — HuggingFace Spaces Version

This is the **Gradio version** of Visatra for HuggingFace Spaces deployment.

## Features

- 📷 **Webcam capture** → YOLO detection + hand gesture recognition
- 🖼️ **Image upload** → real-time detection
- 🎥 **Video upload** → frame-by-frame processing
- ✌️ **Peace gesture** → Gaussian blur effect
- ✋ **Open palm** → blur OFF

## Usage

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Download MediaPipe model:
```bash
curl -o ../models/hand_landmarker.task https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task
```

3. Run:
```bash
python app.py
```

## Deploy to HuggingFace Spaces

1. Create new Space on [huggingface.co](https://huggingface.co/spaces)
2. Select **Gradio** runtime
3. Upload this folder
4. Space will auto-launch

## File Structure

- `app.py` — Main Gradio application
- `detector.py` — YOLO detection logic
- `gesture.py` — MediaPipe hand detection
- `drawing.py` — OpenCV utilities
- `requirements.txt` — Python dependencies

## Notes

- Processing is on-demand (not real-time streaming)
- Webcam captures single frame, processes, returns result
- Video processing may take time depending on duration and system specs

---

**Visatra** — Vision + Satria | [GitHub](https://github.com/satpou/Visatra)
