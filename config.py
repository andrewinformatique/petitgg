import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'petits_gazouillis.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BD_TABLES_EFFACER = os.environ.get('BD_TABLES_EFFACER') or ['publications', 'utilisateur']    
    BD_TABLES_CREER = os.environ.get('BD_TABLES_CREER') or ['utilisateur', 'publications']