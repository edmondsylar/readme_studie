from app_data import received_orders, order, today
from flask import Flask, jsonify, request, make_response


class my_route_data:
    def __init__(self):
        self.id = len(received_orders)+1

# This creates a new order.
    def create_order(self):
        order = {
            'id':len(received_orders)+1,
            'by':request.json['by'],
            'when':today,
            'status':request.json['status'],
            'order':request.json['order']

        }
        received_orders.append(order)


# This gets an order by id.
    def get_order_by_id(self, id):
        try:
            new = [
                each for each in received_orders if each['id'] == id
            ]
            return jsonify({'order {}'.format(id): new[0]}), 200

        except IndexError:
            return jsonify({'error':'Not found!'}), 400 


# This updates an order's Status 
    def update(self, id):
        try:
            new = [x for x in received_orders if x['id'] == id ]
            if x['status'] == 'Done':
                return jsonify({'order with id {}.format(id)':'was already marked done....'})
            else:
                new[0]['status'] = request.json['status']
                return make_response('The update was successfull')

        except IndexError:
            return jsonify({'error':'Somethong Went wrong!'}), 404

        except UnboundLocalError:
            return jsonify({'Error!(UnboundLocalError) ': 'Please check if you have any order with id {} or if your exists'.format(id)})

        
    def get_all_orders(self):
        return received_orders

    def delete_order(self, id):
        try:
            new = [x for x in received_orders if x['id'] == id]
            received_orders.remove(new[0])
            return jsonify({'msg':'order deleted....'})

        except IndexError:
            return jsonify({'error':'sory order not found!'})