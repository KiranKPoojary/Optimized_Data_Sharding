from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
from sharding import perform_sharding
from metadata import get_metadata
import os
import threading
import time
import logging


app = Flask(__name__)

# Enable CORS for all routes
CORS(app, resources={r"/*": {"origins": "*"}})

# Configuration
UPLOAD_FOLDER = 'uploads'
SHARDS_FOLDER = 'shards'
ALLOWED_EXTENSIONS = {'csv'}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(SHARDS_FOLDER, exist_ok=True)

sharding_status = {"status": "Idle", "message": ""}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    if file.filename == '' or not allowed_file(file.filename):
        return jsonify({"error": "Invalid file type"}), 400

    filename = secure_filename(file.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    return jsonify({"message": "File uploaded successfully", "filename": filename}), 200


@app.route('/start_sharding', methods=['POST'])
def start_sharding():
    global sharding_status
    filename = request.json.get('filename')
    algorithm = request.json.get('algorithm')

    if not filename or not algorithm:
        return jsonify({"error": "Filename or algorithm is missing"}), 400

    filepath = os.path.abspath(os.path.join(UPLOAD_FOLDER, filename))
    logging.debug(f"Sharding started for file: {filepath} using algorithm: {algorithm}")

    if not os.path.exists(filepath):
        logging.error(f"File not found: {filepath}")
        return jsonify({"error": f"File '{filename}' not found at {filepath}"}), 400

    def shard_task():
        global sharding_status
        sharding_status['status'] = "In Progress"
        sharding_status['message'] = f"Sharding using {algorithm} started..."
        time.sleep(2)  # Simulating delay

        perform_sharding(filepath, algorithm)
        sharding_status['status'] = "Completed"
        sharding_status['message'] = "Sharding completed successfully!"

    threading.Thread(target=shard_task).start()
    return jsonify({"message": "Sharding started", "status": "In Progress"})


@app.route('/sharding_status', methods=['GET'])
def get_sharding_status():
    return jsonify(sharding_status)


@app.route('/results', methods=['GET'])
def get_results():
    metadata = get_metadata()
    return jsonify(metadata)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
