from flask import Flask, render_template, send_from_directory
from pathlib import Path

UPLOAD_FOLDER = Path("static/uploads")
UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)

def create_app():
    app = Flask(__name__)
    app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024

    # Register blueprints
    from app.routes.webcam import webcam_bp
    from app.routes.upload import upload_bp
    from app.routes.status import status_bp
    app.register_blueprint(webcam_bp)
    app.register_blueprint(upload_bp)
    app.register_blueprint(status_bp)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/uploads/<filename>')
    def uploaded_file(filename):
        return send_from_directory('static/uploads', filename)

    return app