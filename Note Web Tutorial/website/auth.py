from flask import Blueprint 

auth = Blueprint('auth', __name__)
#Defines Blueprint

@auth.route('/')
def home():
    return "<h1>Test</h1>"