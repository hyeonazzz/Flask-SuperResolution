import os, sys
from flask import Flask, render_template, redirect, url_for, request, escape, Response, g, make_response
from werkzeug.utils import secure_filename

UPLOAD_DIR = 'static/images'
app = Flask(__name__)
app.config['UPLOAD_DIR'] = UPLOAD_DIR

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fdbpn_get')
def fdbpn_get():
    return render_template('fdbpn_get.html')

@app.route('/fdbpn_post', methods = ['GET', 'POST'])
def fdbpn_post():
    if request.method == "POST":
        f = request.files['user_img']
        fname = secure_filename(f.filename)
        path = os.path.join(app.config['/user_img/'], fname)
        f.save(path)
    return render_template('fdbpn_post.html', user_img=user_img)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")


