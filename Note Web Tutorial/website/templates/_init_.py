from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'LEXBATS'

    return app
#Created a flask application 
#Initialized it's secret key