from flask import Flask, render_template

app = Flask (__name__)

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