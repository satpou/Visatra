# 🎯 Visatra — Vision + Satria

Aplikasi **Real-Time Object Detection** menggunakan Python, Flask, OpenCV, YOLOv8, dan MediaPipe. Deteksi objek real-time dari webcam, gambar, dan video, plus gesture hand blur.

**Deploy**: Railway.app | **UI**: Web (Flask + Bootstrap 5)

---

## ✨ Features

- 📷 Webcam real-time detection + hand gesture blur
- 🖼️ Upload image → YOLO detection
- 🎥 Upload video → frame-by-frame YOLO detection
- ✌️ **Peace gesture** → Gaussian blur ON
- ✋ **Open palm** → Gaussian blur OFF
- 📊 FPS counter, hand landmark overlay
- ⚡ Frame skipping untuk performa
- 🖥️ Responsive dark-theme UI (desktop + mobile)

---

## 🛠️ Tech Stack

- Python 3.9+
- Flask + Gunicorn
- OpenCV
- Ultralytics YOLOv8
- MediaPipe Hand Landmarker
- PyTorch
- Bootstrap 5
- Railway.app

---

## 📁 Project Structure

```
.
├── app/                     # Flask application (server version)
│   ├── __init__.py          # Flask app factory
│   ├── routes/
│   │   ├── webcam.py        # Video feed (MJPEG)
│   │   ├── upload.py        # Image/video upload API
│   │   └── status.py        # Mode & status API
│   ├── services/
│   │   ├── camera.py        # Camera init & read
│   │   ├── detector.py      # YOLO detection
│   │   ├── gesture.py       # MediaPipe hand detection
│   │   └── stream.py        # MJPEG streaming generator
│   └── utils/
│       └── drawing.py       # OpenCV drawing helpers
├── spaces/                  # Gradio application (HuggingFace Spaces)
│   ├── app.py               # Gradio main app
│   ├── detector.py          # YOLO detection
│   ├── gesture.py           # MediaPipe hand detection
│   ├── drawing.py           # OpenCV utilities
│   ├── requirements.txt     # HF Spaces dependencies
│   └── README.md            # HF Spaces docs
├── models/
│   ├── yolov8s.pt           # YOLO weights
│   └── hand_landmarker.task # MediaPipe model
├── static/
│   ├── style.css
│   ├── script.js
│   └── upload.js
├── templates/
│   └── index.html
├── main.py                  # Flask entry point
├── Procfile                 # Railway process
├── railway.json             # Railway config
├── requirements.txt
└── readme.md
```

---

## 🚀 Installation

Clone:

```bash
git clone https://github.com/satpou/Visatra
cd Visatra
```

Virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# .venv\Scripts\activate   # Windows
```

Dependencies:

```bash
pip install -r requirements.txt
```

Download model:

```bash
curl -o models/hand_landmarker.task https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task
```

---

## 🚀 Run

```bash
python main.py
```

Buka: `http://localhost:5001`

---

## ⚙️ Konfigurasi

| Parameter | File | Keterangan |
|-----------|------|------------|
| `MODEL_PATH` | `app/services/detector.py` | Lokasi model YOLO |
| `CONF_THRESH` | `app/services/detector.py` | Minimum confidence (0.25) |
| `IOU_THRESH` | `app/services/detector.py` | IoU threshold (0.45) |
| `IMG_SIZE` | `app/services/detector.py` | Ukuran input YOLO (640) |
| `SKIP_FRAMES` | `app/services/stream.py` | Frame skip untuk YOLO (2) |

---

## 🖐️ Gesture

| Gesture | Action |
|---------|--------|
| **Peace (✌️)** | Blur ON |
| **Open Palm (✋)** | Blur OFF |

---

## 🚢 Deploy

### Option 1: HuggingFace Spaces (Recommended for free tier)

1. Go to [huggingface.co/spaces](https://huggingface.co/spaces)
2. Create new Space → Select **Gradio** runtime
3. Upload the `spaces/` folder contents
4. Space will auto-launch with GPU support (free)
5. Access via shared link

**Advantages**: Free GPU, no credit card required, auto-deploy from GitHub

**Note**: Processing is on-demand (capture frame → process → return result), not real-time streaming.

See [spaces/README.md](spaces/README.md) for details.

### Option 2: Railway.app (Self-hosted Flask)

1. Push ke GitHub
2. Buka [railway.app](https://railway.app) → New Project → Deploy from GitHub
3. Set `DEPLOY_MODE=true` di Environment Variables (skip camera init)
4. Done.

**Note**: May hit RAM limits on free tier. Set model to `yolov8n.pt` in `app/services/detector.py` for smaller memory footprint.

---

## 📄 License

**Visatra** — Copyright (c) 2026 Satria Rahmaddhani

Released under the **MIT License**. You are free to use, modify, and distribute this project for any purpose, including commercial use and private deployment, provided that the copyright notice above is included in all copies or substantial portions of the Software.

For full license terms, see [LICENSE](LICENSE).

---

## 👨‍💻 Author

**Satria Rahmaddhani** — Visatra (Vision + Satria)

GitHub: https://github.com/satpou/Visatra