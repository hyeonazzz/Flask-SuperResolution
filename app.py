import os, sys
from flask import Flask, render_template, redirect, url_for, request, escape, Response, g, make_response
from werkzeug.utils import secure_filename

UPLOAD_DIR = 'static/images/user_img'
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
        try:
            os.remove('UPLOAD_DIR')
            file_handle.close()
        except Exception as error:
            app.logger.error("Error removing or closing downloaded file handle", error)

        user_img = request.files['user_img']
        fname = secure_filename(user_img.filename)
        path = os.path.join(app.config['UPLOAD_DIR'], fname)
        user_img.save(path)
    return render_template('fdbpn_post.html', user_img=user_img)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")


