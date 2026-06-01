#Setup Flask Application
from flask import Flask

def create_app():  #Create a function
    app = Flask(__name__)  #Initialise app and name of the file that will run
    app.config['SECRET_KEY'] = 'LEXBAT' #Will ecrypt / secure cookies and section data
    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix= '/')
    app.register_blueprint(auth, url_prefix= '/')

    return app
