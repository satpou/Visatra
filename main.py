import os
import sys
from app import create_app
from app.services.detector import init_model
from app.services.gesture import init_landmarker

app = create_app()

# Initialize models at startup (for both gunicorn and python main.py)
init_model()
init_landmarker()

if __name__ == '__main__':
    from app.services.camera import init_camera
    if not os.environ.get('DEPLOY_MODE'):
        init_camera()
    port = int(os.environ.get('PORT', 5001))
    print(f"[INFO] Server ready at http://0.0.0.0:{port}")
    app.run(host='0.0.0.0', port=port, debug=False, threaded=True)