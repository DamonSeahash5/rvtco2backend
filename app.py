import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = "./uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
ALLOWED_EXTENSIONS = {"rvt",}

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
CORS(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# check file extension
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# receive a .rvt file via POST and save it
@app.route("/upload", methods=["POST"])
def file_save():
    # response_obj = {}
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename=secure_filename(file.filename)
        # note to secure filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return jsonify({"status": "success", "filename": filename})
    return jsonify({"status": "success", "filename": filename})