from flask import Blueprint, jsonify, request
from sql_alchemy_db_instance import db
from models import MuseumActivities, MuseumInfo

museum_api = Blueprint('museum_api', __name__)


@museum_api.route('/home', methods=['GET'])
def view_all_museum_activities():
    activity_instances = db.session.query(MuseumActivities).all()
    activity_examples = [{"id": activity.id, "museum_id": activity.museum_id,
                          "activity_name": activity.activity_name, "activity_descrip": activity.activity_description,
                          "num_kids_taken": activity.number_of_kids_taken,
                          "low_age_range": activity.low_age_range_of_child_taken,
                          "high_age_range": activity.high_age_range_of_child_taken} for activity in activity_instances]
    return jsonify({"activities": activity_examples})


@museum_api.route('/add-museum', methods=['POST'])
def add_new_museum():
    new_museum = MuseumInfo()
    new_museum.museum_name = request.json["museum_name"]
    new_museum.museum_city = request.json["museum_city"]
    db.session.add(new_museum)
    db.session.commit()

    return jsonify(success=True)


@museum_api.route('/museum', methods=['GET'])
def view_all_museums():
    museum_instances = db.session.query(MuseumInfo).all()
    museum_list = [{"id": museum.id, "museum_name": museum.museum_name,
                    "museum_city": museum.museum_city} for museums in museum_instances]
    return jsonify({"museums": museum_list})


@museum_api.route('/add-activity', methods=['POST'])
def add_new_activity():
    new_activity = MuseumActivities()
    new_activity.museum_id = request.json["museum_id"]
    new_activity.activity_name = request.json["activity_name"]
    new_activity.activity_description = request.json["activity_descrip"]
    new_activity.number_of_kids_taken = request.json["number_of_kids_taken"]
    new_activity.low_age_range_of_child_taken = request.json["low_age_range_of_child_taken"]
    new_activity.high_age_range_of_child_taken = request.json["high_age_range_of_child_taken"]
    db.session.add(new_activity)
    db.session.commit()

    return jsonify(success=True)


@museum_api.route('/add-activity', methods=['PATCH'])
def delete_activity():
    activity_id = request.json["id"]
    target_activity = db.session.query(
        MuseumActivities).filter_by(id=activity_id).first()
    db.session.add(target_todo)
    # why is above not .delete method?
    db.session.commit()
    return jsonify(success=True)
