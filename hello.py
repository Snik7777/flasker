from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime





app = Flask (__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:cars$sinks**p1@localhost/our_users'

app.config['SECRET_KEY'] = "A"

db = SQLAlchemy(app)
class users(db.Model):
	id= db.column(db.Integer, primary_key=True)
	name = db.column(db.String(200), nullable=False)
	email = db.column(db.String(200), nullable=False, inique=True)
	date_added = db.column(db.DateTime, default=datetime.utcnow)
	
	def __repr__(self):
		return '<Name %r>' % self.name

class UserForm(FlaskForm):
	name = StringField("Name", validators=[DataRequired()])
	email = StringField("Email", validators=[DataRequired()])
	submit = SubmitField("Submit")




class NameForm(FlaskForm):
	name = StringField("whats yours name", validators=[DataRequired()])
	submit = SubmitField("Submit")


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
	form = UserForms()
	name_to _updat= users.query.gry_or_404(id)
	if request.method == "POST":
		name_to_update.name = request.form['name']
		name_to_update.email = request.form['email']
		try:
			db.session.commit()
			flash ("added")
			return render_template("update.html", form=form, name_to_update=name_to_update)

        except:
        	flash ("try again")
			return render_template("update.html", form=form, name_to_update=name_to_update)


    else:
    	flash ("added")
			return render_template("update.html", form=form, name_to_update=name_to_update)



@app.route('/user/add', methods=['GET','POST'])
def add_user():
	name = None
	form = UserForm()
	if form.validate_on_submit():
		user = Users.query.filter_by(email=form.email.data).first()
		if user is None:
			user = Users(name=form.name.data, email=form.email.data)
			db.session.add(user)
			db.session.commit()
		name = form.name.data
		form.name.data = ''
		form.email.data = ''
		flash("added successfuly")
	our_users = Users.query.order_by(Users.date_added) 
	return render_template("ass_user.html", form=form, name=name, our_users=our_users)
		




@app.route('/')

def index():
	favorite_pizza = ["a", "b", "c", 41]
	first_name = "john"
	return render_template("index.html", first_name=first_name, favorite_pizza=favorite_pizza)


@app.route('/user/<name>')

def user(name):
	return render_template("user.html", user_name=name)



@app.errorhandler(404)

def page_not_found(e):
	return render_template("404.html"),404

@app.errorhandler(500)

def page_not_found(e):
	return render_template("500.html"),500	


@app.route('/name', methods=['GET', 'POST'])
def name():
	name = None
	form = NameForm()
	if form.validate_on_submit():
		name=form.name.data
		form.name.data = ''
		flash("form submitted successfuly")
	return render_template("name.html", name=name, form=form)

