from flask import Flask


def create_app(test_config=None):
    # WIN COMMANDS:
    # create and configure the app
    # $set FLASK_APP=flaskr
    # $set FLASK_ENV=development
    # $flask run
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    from . import dates
    app.register_blueprint(dates.bp)

    from . import numbers
    app.register_blueprint(numbers.bp)

    from . import mimificator
    app.register_blueprint(mimificator.bp)

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Primeiros exercícios'

    return app