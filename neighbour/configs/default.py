# -*- coding: utf-8 -*-


class DefaultConfig(object):
    DEBUG = True
    TESTING = False

    SEND_LOG = False

    SQLALCHEMY_DATABASE_URI = ''

    # This will print all SQL statements
    SQLALCHEMY_ECHO = True

    # Security
    # This is the secret key that is used for session signing.
    # You can generate a secure key with os.urandom(24)
    SECRET_KEY = 'secret key'

    # Protection against form post fraud
    WTF_CSRF_ENABLED = True
    WTF_CSRF_SECRET_KEY = "reallyhardtoguess"