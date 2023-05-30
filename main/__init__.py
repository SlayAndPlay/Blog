from main.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask import Flask
from flask_login import LoginManager
from flask_mail import Mail
                                        # Name of the module - in this case "main"
                                        # If script is run directly, __name__ will return __main__
                                        # Else if ran via import, the name of the python file will show

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from main.users.routes import users
    from main.misc.routes import misc
    from main.posts.routes import posts
    from main.errors.handlers import errors

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(misc)
    app.register_blueprint(errors)

    return app
