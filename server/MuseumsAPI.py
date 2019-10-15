from flask import Blueprint, jsonify, request
from sql_alchemy_db_instance import db
from models import Museum_Activities, Museum_Info

museum_api = Blueprint('museum_api', __name__)


@museum_api.route('/home', methods=['GET'])
def view_all_museum_activities():
    activity_instances = db.session.query(Museum_Activities).all()
    activity_examples = [{"id": activity.id, "museum_id": activity.museum_id,
                          "activity_name": activity.activity_name, "activity_descrip": activity.activity_description, "num_kids_taken": activity.number_of_kids_taken, "low_age_range": activity.low_age_range_of_child_taken, "high_age_range": activity.high_age_range_of_child_taken} for activity in activity_instances]
    return jsonify({"activities": activity_examples})


@museum_api.route('/add-activity', methods=['POST'])
def add_new_activity():
    new_activity = Museum_Activities()
    new_activity.activity_name = request.json["activity_name"]
    new_activity.activity_description = request.json["activity_descrip"]
    new_activity.number_of_kids_taken = request.json["number_of_kids_taken"]
    new_activity.low_age_range_of_child_taken = request.json["low_age_range_of_child_taken"]
    new_activity.high_age_range_of_child_taken = request.json["high_age_range_of_child_taken"]
    db.session.add(new_activity)
    db.session.commit()
    return jsonify(success=True)
