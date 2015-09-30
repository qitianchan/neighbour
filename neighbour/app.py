# -*- coding: utf-8 -*-
from flask import Flask
from neighbour.district.views import distric
from neighbour.wechat.navbar import wechat_navbar
from neighbour.extensions import db
from neighbour.commodity.models import Product
from flask_sqlalchemy import SQLAlchemy


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
    app.debug = app.config['DEBUG']
    return app
# app = Flask(__name__)
# db = SQLAlchemy(create_app())

def configure_blueprint(app):
    app.register_blueprint(distric)
    app.register_blueprint(wechat_navbar)


def configure_extensions(app):
    # Flask-SQLAlchemy
    db.init_app(app)
    db.app = app

if __name__ == '__main__':
    app = create_app()
    db.create_all()
    product = Product.query.filter_by(product_id=1).first()
    if product:
        print product.orginal_price
    else:
        print u'不存在该数据'
