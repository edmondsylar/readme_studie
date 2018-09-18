class orders:
    def __init__(self):
        self.order_list = [
            {
                'id':1,
                'status':'Done',
                'By':'username'
            }
        ]

    def get_all(self):
        return self.order_list