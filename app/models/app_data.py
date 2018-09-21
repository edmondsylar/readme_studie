import time
from flask import jsonify

today = time.ctime()
received_orders = []
order = dict()
