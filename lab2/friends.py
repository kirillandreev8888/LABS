import baseclass

import requests


class friends(baseclass.BaseClient):
    BASE_URL = 'https://api.vk.com/method/'
    method='friends.get'
    def _get_data(self, id):
        t = requests.get(friends.BASE_URL+friends.method+'?user_id=' + str(id) + '&fields=bdate&v=5.62').json()
        return t
    def response_handler(self, t):
        a= t["response"]['items']

        return a


