# app.py
from flask import Flask, jsonify, send_from_directory

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
    return "Hello, World!\n"

@app.route('/download/<path:filename>')
def download_file(filename):
    # serve file from the project's root directory
    return send_from_directory('.', filename, as_attachment=True)

# optional JSON endpoint
@app.route("/json", methods=["GET"])
def hello_json():
    return jsonify(message="Hello, World!")

if __name__ == "__main__":
    # debug=True for development only
    app.run(host="0.0.0.0", port=5000, debug=True)
