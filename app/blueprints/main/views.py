from .import bp as main
from flask import render_template

@main.route('/', methods=['GET'])
def home():
    return render_template('home.html')