from flask import Flask, render_template
# to run, 'source virt/bin/activate'
# flask run

# Create a flask instance

app = Flask(__name__)

# Create a route decorator


@app.route('/')
# def index():
# return "<h1>Hello World!</h1>"

# FILTERS!
# safe
# capitalize
# upper
# title
# trim
# striptags


def index():
    first_name = 'John'
    stuff = 'This is bold text'
    favorite_pizza = ["Pepperoni", "cheese", "Mushrooms", 42]
    return render_template('index.html', first_name=first_name, stuff=stuff, favorite_pizza=favorite_pizza)

# localhost:5000/user/john


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', user_name=name)
