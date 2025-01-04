from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
from sharding import perform_sharding
from metadata import get_metadata
import os
import threading
import time
import logging
from datetime import datetime

app = Flask(__name__)

# Enable CORS for all routes
CORS(app, resources={r"/*": {"origins": "*"}})

# Configuration
UPLOAD_FOLDER = 'uploads'
SHARDS_FOLDER = 'shards'
ALLOWED_EXTENSIONS = {'csv'}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(SHARDS_FOLDER, exist_ok=True)

# Global variables to track the sharding status and start time
sharding_status = {"status": "Idle", "message": "", "elapsed_time": 0}
sharding_start_time = None  # To store the start time of the sharding process


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
    global sharding_status, sharding_start_time
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
        global sharding_status, sharding_start_time
        # Update the sharding status to "In Progress"
        sharding_status['status'] = "In Progress"
        print(sharding_status['status'])
        sharding_status['message'] = f"Sharding using {algorithm} started..."

        # Capture the start time when sharding begins
        sharding_start_time = datetime.now()
        logging.debug(f"Sharding started at {sharding_start_time}")
        print(f"Sharding started at {sharding_start_time}")

        time.sleep(2)  # Simulating a delay (sharding process)

        perform_sharding(filepath, algorithm)  # Perform the actual sharding
        # After sharding is complete, update the status
        sharding_status['status'] = "Completed"
        print(sharding_status['status'])
        sharding_status['message'] = "Sharding completed successfully!"

        # Reset the elapsed time after completion
        sharding_status['elapsed_time'] = 0






    threading.Thread(target=shard_task).start()
    return jsonify({"message": "Sharding started", "status": "In Progress"})


@app.route('/sharding_status', methods=['GET'])
def get_sharding_status():
    global sharding_status, sharding_start_time

    # Calculate the elapsed time for "In Progress" status
    if sharding_status["status"] == "In Progress" and sharding_start_time:
        elapsed_time = (datetime.now() - sharding_start_time).seconds
        sharding_status["elapsed_time"] = elapsed_time

    return jsonify(sharding_status)


@app.route('/results', methods=['GET'])
def get_results():
    metadata = get_metadata()  # This function fetches the metadata
    return jsonify(metadata)


@app.route('/reset_sharding', methods=['POST'])
def reset_sharding():
    global sharding_status
    # Reset the sharding status and any other server-side data
    sharding_status = {"status": "Idle", "message": ""}

    # Optionally, clear the uploaded files or other data


    return jsonify({"message": "Sharding has been reset to idle state."}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
