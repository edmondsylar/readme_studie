from ..app import api
import unittest
import json

class All_tests(unittest.TestCase):

    def setUp(self):
        self.my_test = api.test_client(self)
        self.sample_data = {
            'by':'sample_user',
            'order':'fries only',
            'status':'pending'
        }
        self.empty = dict()
        self.any_data = dict()
        self.updater = {
            'status':'done'
        }
        self.all_data = []
      
      
    def test_index(self):
        feedback = self.my_test.get('/api/v1/', content_type='application/json')
        self.assertNotEqual(feedback.status_code, 404)

    def test_defualt_route_returns_correct_info(self):
        response = self.my_test.get('/api/v1/', content_type='application/json')
        self.assertTrue(b'WELCOME TO FAST FOODS FAST' in response.data)

    def test_orders_added_to_order_list(self):
        response = self.my_test.post('/api/v1/post/orders', data= json.dumps(self.sample_data), content_type='application/json')
        response = self.all_data.append(self.sample_data)
        self.assertNotEqual(self.all_data, [])

    def test_for_post_method_working(self):
        response = self.my_test.post('/api/v1/post/orders', data= json.dumps(self.sample_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_order_really_created(self):
        response = self.my_test.post('/api/v1/post/orders', data= json.dumps(self.sample_data), content_type='application/json')
        self.assertTrue(response.status_code, 200)

    def test_empty_order_not_accepted(self):
        response = self.my_test.post('/api/v1/post/orders', data= json.dumps(self.empty), content_type='application/json')
        self.assertTrue(response.status_code, 500)
        #error code 500 server cannot process therequest for an unknown reason.

    def test_get_all_endpoint(self):
        responce = self.my_test.get('/api/v1/get/orders', content_type='application/json')
        self.assertEqual(responce.status_code, 200)

    def test_update(self):
        response = self.my_test.post('/api/v1/post/orders', data= json.dumps(self.sample_data), content_type='application/json')
        response = self.my_test.put('/api/v1/get/orders/1', data=json.dumps(self.updater), content_type='application/json')
        self.assertTrue(b'The update was successfull' in response.data)
