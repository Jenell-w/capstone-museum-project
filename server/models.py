from sql_alchemy_db_instance import db
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import ForeignKey


class MuseumActivities(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    museum_id = db.Column(db.Integer, db.ForeignKey(
        'museum_info.id'), nullable=False)
    activity_name = db.Column(db.String(500))
    activity_description = db.Column(db.String(500))
    number_of_kids_taken = db.Column(db.Integer)
    low_age_range_of_child_taken = db.Column(db.Integer)
    high_age_range_of_child_taken = db.Column(db.Integer)


class MuseumInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    museum_name = db.Column(db.String(200))
    museum_city = db.Column(db.String(200))

# problem is: how to use sessions in python so as to delete all data from table.
