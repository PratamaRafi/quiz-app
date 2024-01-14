import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:Muhrafi123.@localhost/quiziz'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    QUES_PER_PAGE = 1