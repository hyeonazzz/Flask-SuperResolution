import os, sys
from
from flask import Flask, render_template, redirect, url_for, request, escape, Response, g, make_response
from werkzeug.utils import secure_filename
sys.path.append('DBPN')
import eval.py


UPLOAD_DIR = 'static/images/user_img'
app = Flask(__name__)
app.config['UPLOAD_DIR'] = UPLOAD_DIR

def removeAllFile(filePath):
    if os.path.exists(filePath):
        for file in os.scandir(filePath):
            os.remove(file.path)
        else:
            return 'already clean'
print('os.remove')

removeAllFile('static/images/user_img')
removeAllFile('static/images/output/user_img')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fdbpn_get')
def fdbpn_get():
    return render_template('fdbpn_get.html')

@app.route('/fdbpn_post', methods = ['GET', 'POST'])
def fdbpn_post():
    if request.method == "POST":
        user_img = request.files['user_img']
        fname = secure_filename(user_img.filename)
        path = os.path.join(app.config['UPLOAD_DIR'], fname)
        user_img.save(path)
        eval()
    return render_template('fdbpn_post.html', user_img=user_img)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")


