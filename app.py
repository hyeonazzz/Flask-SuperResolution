import os, sys
from flask import Flask, render_template, redirect, url_for, request, escape, Response, g, make_response
from werkzeug.utils import secure_filename
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fdbpn_get')
def fdbpn_get():
    return render_template('fdbpn_get.html')

@app.route('/fdbpn_post', methods = ['GET', 'POST'])
def fdbpn_post():
    if request.method == "POST":
        for f in os.scandir('static/images/user_img'):
            os.remove(f.path)

        user_img = request.files.getlist('user_img')

        upload_files['user_img'] = []

        for f in face_file:
            if f:
                f.save('static/images/user_img2/'+secure_filename(f.filename))
                upload_files['user_img'].append(f.filename)
    time.sleep(2)
    return render_template('fdbpn_post.html', user_img=user_img)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")


