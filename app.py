import os, sys
import time
from flask import Flask, render_template, redirect, url_for, request, escape, Response, g, make_response
from werkzeug.utils import secure_filename
sys.path.append('DBPN')

UPLOAD_DIR = 'static/images/user_img'
app = Flask(__name__)
app.config['UPLOAD_DIR'] = UPLOAD_DIR

def removeInput(filePath):
    if os.path.exists(filePath):
        for file in os.scandir(filePath):
            os.remove(file.path)
        else:
            return 'already clean'
print('in.remove')

def removeOutput(filePath):
    if os.path.exists(filePath):
        for file in os.scandir(filePath):
            os.remove(file.path)
        else:
            return 'already clean'
print('out.remove')

removeInput('static/images/user_img')
removeOutput('static/images/output/user_img')

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

        #output_img = eval.
        #output_img = request.files['output/user_img']
        fname = secure_filename(output_img.filename)
    return render_template('fdbpn_post.html', user_img=user_img, output_img=output_img)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", debug=True)


