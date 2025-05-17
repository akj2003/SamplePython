from flask import Flask, render_template, request, redirect, url_for, jsonify
import os
from db_helper import insert_file_metadata

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB limit

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file part", 400
        file = request.files['file']
        if file.filename == '':
            return "No selected file", 400
        if file:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            # Save file metadata to the database
            insert_file_metadata(file.filename)
            return "File uploaded successfully", 200
    return render_template('upload.html')
