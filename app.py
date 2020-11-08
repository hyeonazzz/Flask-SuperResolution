import os
from flask import Flask, render_template, redirect, url_for, request
from werkzeug.utils import secure_filename
app = Flask(__name__)

uploads_dir = os.path.join(app.instance_path, 'static/img/user_img')
os.makedirs(uploads_dir, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fdbpn_get')
def fdbpn_get():
    return render_template('fdbpn_get.html')

@app.route('/fdbpn_post', methods = ['GET', 'POST'])
def fdbpn_post():
    global user_img
    if request.method == 'POST':
        user_img = request.files['user_img']
        profile.save(os.path.join(uploads_dir, secure_filename(user_img.filename)))

    return render_template('fdbpn_post.html', user_img=user_img)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")


