from sql_alchemy_db_instance import db
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey


class Museum_Activities(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    museum_id = db.Column(db.Integer)
    activity_name = db.Column(db.String(500))
    activity_description = db.Column(db.String(500))
    number_of_kids_taken = db.Column(db.Integer)
    low_age_range_of_child_taken = db.Column(db.Integer)
    high_age_range_of_child_taken = db.Column(db.Integer)

    museum_info = relationship(
        "Museum_Info", foreign_keys="[museum_id]")


class Museum_Info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    museum_id = db.Column(db.Integer, ForeignKey(
        'Museum_Activities.museum_id'))
    museum_name = db.Column(db.String(200))
    museum_city = db.Column(db.String(200))
    child_friendly = db.Column(db.Boolean)
