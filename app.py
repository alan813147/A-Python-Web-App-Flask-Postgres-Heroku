from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_mail

app = Flask(__name__)

ENV = 'prod'

if ENV == 'dev':
    app.debug = True
    app.config ['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1218@localhost/pvtkit'
else:
    app.debug = False
    app.config ['SQLALCHEMY_DATABASE_URI'] = 'postgresql://odbnejngfmuuwk:05c5f256c2a26a76977a77248fce7e61344e3737505c41697701e52f392bddaa@ec2-3-224-184-9.compute-1.amazonaws.com:5432/d4bebk48ntrth'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(200), unique=True)
    waiter = db.Column(db.String(200))
    rating = db.Column(db.Integer)
    comments = db.Column(db.Text())

    def __init__(self, customer, waiter, rating, comments):
        self.customer = customer
        self.waiter = waiter
        self.rating = rating
        self.comments = comments



@app.route('/')

def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        customer = request.form['customer']
        waiter = request.form['waiter']
        rating = request.form['rating']
        comments = request.form['comments']
        # print(custmer, waiter, rating, comments)
        if customer == '' or waiter =='':
            return render_template('index.html',message='Pls enter required fields')
        if db.session.query(Feedback).filter(Feedback.customer == customer).count() == 0:
            data = Feedback(customer, waiter, rating, comments)
            db.session.add(data)
            db.session.commit()
            send_mail(customer, waiter, rating, comments)
            return render_template('success.html')
        return render_template('index.html',message='You have already submitted feedback')
        

if __name__=='__main__':
    # app.debug = True ##重開會是新的頁面
    app.run()