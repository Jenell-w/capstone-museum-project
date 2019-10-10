from flask import Blueprint, jsonify, request
from sql_alchemy_db_instance import db
from models import Museum_Activities

museum_api = Blueprint('museum_api', __name__)


# we don't need methods if we are not getting data from this page?
@museum_api.route('/home')
# def view_all_museums():
