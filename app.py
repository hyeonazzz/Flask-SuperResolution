from flask import Flask, render_template, redirect, url_for, request
from werkzeug import secure_filename
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
    
@app.route('/result')
def result():
    return render_template('result.html')


@app.route('/fileUpload', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save('Uploads/'+ secure_filename(f.filename))
        return render_template('result.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")


