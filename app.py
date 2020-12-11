import os, sys
import time
from flask import Flask, render_template, redirect, url_for, request, escape, Response, g, make_response
from werkzeug.utils import secure_filename
from mode import *
import argparse

parser = argparse.ArgumentParser()

def str2bool(v):
    return v.lower() in ('true')

parser.add_argument("--LR_path", type = str, default = 'static/images/user_img')
parser.add_argument("--GT_path", type = str, default = '')
parser.add_argument("--res_num", type = int, default = 16)
parser.add_argument("--num_workers", type = int, default = 0)
parser.add_argument("--batch_size", type = int, default = 16)
parser.add_argument("--L2_coeff", type = float, default = 1.0)
parser.add_argument("--adv_coeff", type = float, default = 1e-3)
parser.add_argument("--tv_loss_coeff", type = float, default = 0.0)
parser.add_argument("--pre_train_epoch", type = int, default = 8000)
parser.add_argument("--fine_train_epoch", type = int, default = 4000)
parser.add_argument("--scale", type = int, default = 4)
parser.add_argument("--patch_size", type = int, default = 24)
parser.add_argument("--feat_layer", type = str, default = 'relu5_4')
parser.add_argument("--vgg_rescale_coeff", type = float, default = 0.006)
parser.add_argument("--fine_tuning", type = str2bool, default = False)
parser.add_argument("--in_memory", type = str2bool, default = True)
parser.add_argument("--generator_path", type = str, default = 'model/SRGAN.pt')
#parser.add_argument("--generator_path", type = str, default = 'model/SRGAN_11500_201124.pt')
parser.add_argument("--mode", type = str, default = 'test_only')

args = parser.parse_args()



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
    removeInput('static/images/user_img')
    removeOutput('static/images/output/user_img')
    return render_template('index.html')

@app.route('/result', methods = ['GET', 'POST'])
def result():
    if request.method == "POST":
        global user_img
        user_img = request.files['user_img']
        fname = secure_filename(user_img.filename)
        nonext, ext = fname.split(sep='.')

        if ext == 'png':
            path = os.path.join(app.config['UPLOAD_DIR'], 'upload.png')
            user_img.save('static/images/user_img/upload.png')
        
        elif ext == 'jpg':
            path = os.path.join(app.config['UPLOAD_DIR'], 'upload.jpg')
            user_img.save('static/images/user_img/upload.jpg')
        
        elif ext == 'bmp':
            path = os.path.join(app.config['UPLOAD_DIR'], 'upload.bmp')
            user_img.save('static/images/user_img/upload.bmp')

        else :
            print('extension not found')

        if args.mode == 'train':
            train(args)
    
        elif args.mode == 'test':
            test(args)
    
        elif args.mode == 'test_only':
            test_only(args)
    return render_template('result.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", debug=True)


