import os
from flask import Flask, render_template, redirect, url_for, request
from werkzeug.utils import secure_filename
app = Flask(__name__)

uploads_dir = os.path.join(app.instance_path, 'uploads')
os.makedirs(uploads_dir, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods = ['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # save the single "profile" file
        profile = request.files['file']
        profile.save(os.path.join(uploads_dir, secure_filename(profile.filename)))

    return render_template('upload.html')

@app.route('/result')
def result():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")


