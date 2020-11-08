from flask import Flask, render_template, redirect, url_for, request
from werkzeug.utils import secure_filename
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/fileUpload', methos = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save('Uploads/'+ secure_filename(f.filename))
        return 'good'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")


