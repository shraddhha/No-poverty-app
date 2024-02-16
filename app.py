from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(_name_)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///poverty_free.db'
db = SQLAlchemy(app)

class Loan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lender = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    purpose = db.Column(db.String(200), nullable=False)

class Donation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    donor = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)

db.create_all()

@app.route('/')
def index():
    loans = Loan.query.all()
    donations = Donation.query.all()
    courses = Course.query.all()
    jobs = Job.query.all()
    return render_template('index.html', loans=loans, donations=donations, courses=courses, jobs=jobs)

@app.route('/apply_loan', methods=['GET', 'POST'])
def apply_loan():
    if request.method == 'POST':
        lender = request.form['lender']
        amount = request.form['amount']
        purpose = request.form['purpose']
        new_loan = Loan(lender=lender, amount=amount, purpose=purpose)
        db.session.add(new_loan)
        db.session.commit()
        return redirect('/')
    return render_template('apply_loan.html')

# Similar routes for donation, course creation, job posting, etc.

if _name_ == '_main_':
    app.run(debug=True)