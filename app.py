import os, sys
real_path = os.path.dirname(os.path.realpath(__file__))
sub_path = "/".join(real_path.split("/")[:-1])
os.chdir(sub_path)
from flask import Flask, render_template, redirect, url_for, request, escape, Response, g, make_response
from werkzeug.utils import secure_filename
app = Flask(__name__)

uploads_dir = os.path.join(app.instance_path, 'static/img/user_img')
os.makedirs(uploads_dir, exist_ok=True)

def root_path():
	real_path = os.path.dirname(os.path.realpath(__file__))
	sub_path = "\\".join(real_path.split("\\")[:-1])
	return os.chdir(sub_path)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fdbpn_get')
def fdbpn_get():
    return render_template('fdbpn_get.html')

@app.route('/fdbpn_post', methods = ['GET', 'POST'])
def fdbpn_post():
    if request.method == 'POST':
        root_path()

        user_img = request.files['user_img']
		user_img.save('static/img/user_img/'+str(user_img.filename))
		user_img_path = '/user_img/'+str(user_img.filename)

    return render_template('fdbpn_post.html', user_img=user_img)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")


