# This module has all the end points
from flask import Blueprint, request, jsonify, make_response
from ..models.modules import my_route_data
my_blueprint = Blueprint('my_blueprint',__name__)

data = my_route_data()
@my_blueprint.route('/')
def index():
    return 'WELCOME TO FAST FOODS FAST'


@my_blueprint.route('/get/orders', methods = ['GET'])
def get_orders():
    orders = data.get_all_orders()
    return make_response(jsonify({'Orders':orders}))

@my_blueprint.route('/get/orders/<int:id>', methods = ['GET'])
def get_by_id(id):
    retrive = data.get_order_by_id(id)
    return retrive

@my_blueprint.route('/get/orders/<int:id>', methods = ['PUT'])
def update_order(id):
    temp = data.update(id)
    return temp

@my_blueprint.route('/post/orders', methods = ['POST'])
def create_order():
    data.create_order()
    return make_response(jsonify({'msg':'Order Created'}))

@my_blueprint.route('/order/<int:id>', methods = ['DELETE'])
def delete_order(id):
    temp = data.delete_order(id)
    return temp

    