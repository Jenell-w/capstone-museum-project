import os
from flask import Flask, render_template
from MuseumsAPI import museum_api
from sql_alchemy_db_instance import db
from models import MuseumInfo
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from seeds import seed_database_with_museums
import pandas as pd

project_dir = os.path.dirname(os.path.abspath(__file__))
project_paths = project_dir.split("/")
project_paths.pop()
project_paths.append('db')
project_dir = "/".join(project_paths)


def create_app():
    app = Flask(__name__,
                static_folder="./dist/static",
                template_folder="./dist"
                )

    if os.environ["RUN_ENVIRONMENT"] == 'network':
        app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://{user}:{pw}@{url}/{db}".format(
            user=os.environ["DB_USER"], pw=os.environ["DB_PASS"], url=os.environ["DB_URL"], db=os.environ["DB_NAME"])
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///{}".format(
            os.path.join(project_dir, "vue-flask-museum.db"))
    app.config['SQLALCHEMY_ECHO'] = True
    db.init_app(app)
    app.register_blueprint(museum_api)

    return app


def setup_database(app):
    with app.app_context():
        db.create_all()
        try:
            db.session.query(MuseumInfo).one()  # One result, will not seed
        except NoResultFound:
            print("MuesumInfo table is empty so we are seeding")
            seed_database_with_museums()
        except MultipleResultsFound:
            # All is good, there is stuff in the db.
            print("Db contains entries, skipping seed process")
