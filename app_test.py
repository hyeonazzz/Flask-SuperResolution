from flask import Flask, render_template, redirect, url_for, request
from flask_mail import Mail, Message

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/timeline')
def timeline():
    return render_template('timeline.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'flaskpy2019@gmail.com'
app.config['MAIL_PASSWORD'] = 'fromflaskemailpy1!'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True



@app.route("/contact", methods=['post', 'get'])
def email_test():
   
    if request.method == 'POST':
        sendername = request.form['senderwho']
        senders = request.form['email_sender']
        receiver = request.form['email_receiver']
        content = request.form['email_content']
        receiver = receiver.split(',')
        
       
        for i in range(len(receiver)):
            receiver[i] = receiver[i].strip()
       
        result = send_email(senders, receiver, content, sendername)
       
        if not result:
            return render_template('contact.html', content="Email is sent")
        else:
            return render_template('contact.html', content="Email is not sent")
       
    else:
        return render_template('contact.html')
   
def send_email(senders, receiver, content, sendername):
    try:
        mail = Mail(app)
        msg = Message('Title', sender = senders, recipients = receiver)
        msg.body = ("From: {0}\nName: {1}\nContent: {2}".format(senders,sendername,content))
        mail.send(msg)
    except Exception:
        pass
    finally:
        pass

@app.route('/post002')
def post002():
    return render_template('post/post002.html')

@app.route('/post003')
def post003():
    return render_template('post/post003.html')

@app.route('/post004')
def post004():
    return render_template('post/post004.html')

@app.route('/post005')
def post005():
    return render_template('post/post005.html')

@app.route('/post006')
def post006():
    return render_template('post/post006.html')

@app.route('/post007')
def post007():
    return render_template('post/post007.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")


