from flask import Flask
from district.views import distric
from wechat.navbar import wechat_navbar
def create_app(config=None):
    """
    Creates the app
    :param config:
    :return:
    """
    app = Flask(__name__)

    # Use the default config and override it afterwards
    app.config.from_object('neighbour.configs.default.DefaultConfig')
    # Update the config
    app.config.from_object(config)

    configure_blueprint(app)
    configure_extensions(app)
    # configure_extensions(app)
    app.debug = app.config['DEBUG']
    return app


def configure_blueprint(app):
    app.register_blueprint(distric)

    app.register_blueprint(wechat_navbar)


def configure_extensions(app):
    pass

if __name__ == '__main__':
    pass
