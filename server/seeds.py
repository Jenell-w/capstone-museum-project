from sql_alchemy_db_instance import db
from models import MuseumInfo


def seed_database_with_museums():
    with open('museum-names.csv') as f:
        lines = f.readlines()
        lines = lines[1:]
    for line in lines:
        name = line.split(",")[0]
        city = line.split(",")[1]

        new_museum = MuseumInfo()
        new_museum.museum_name = name
        new_museum.museum_city = city
        db.session.add(new_museum)

    db.session.commit()
