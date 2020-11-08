from flask import Flask, render_template, redirect, url_for, request
from werkzeug import secure_filename
app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    return render_template('index.html')

def upload_file();
    if request.method == 'POST':
        f - request.files['file']
        f.save('Uploads/' + secure_filename(f.filename))
        return result
    
@app.route('/result')
def result():
    return render_template('result.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")


