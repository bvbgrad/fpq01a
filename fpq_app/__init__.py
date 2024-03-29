import os

from flask import (
    Flask, render_template)


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'rpi.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    @app.route('/hello/<name>')
    def hello(name=None):
        return render_template('auth/hello.html', name=name)

    # Import and call db.init_app function from the factory
    # so it can be called using the "flask init-db" command
    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import quiz
    app.register_blueprint(quiz.bp)
    app.add_url_rule('/', endpoint='quiz_prep')

    return app
