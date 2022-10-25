from django.test import TestCase
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
import requests

class SampleTest(TestCase):

    def test_string(self):
       a = 'some'
       b = 'some'
       self.assertEqual(a, b)

    def create_user(self):
        user_obj = User.objects.create_user(username='test', password='testtest', email='test@mailinator.com')
        return user_obj

    def setUp(self):
        self.user = self.create_user()

    def test_create_user(self):
        user_obj = User.objects.get(pk=self.user.id)
        self.assertEqual(user_obj.username, 'test')

    def test_update_user(self):
        user_obj = User.objects.get(pk=self.user.id)
        user_obj.username = 'test_user_edit'
        user_obj.save()
        self.assertEqual(user_obj.username, 'test_user_edit')

    def test_api_call(self):
        r = requests.get('https://jsonplaceholder.typicode.com/todos/1')
        self.assertEqual(r.status_code, 200)

class SampleAPITest(APITestCase):

    API_SERVER_URL = "https://qa.goldenfinancing.com"

    def user_auth(self, username, password):
        self.user = self.create_user(username, password)
        return self.client.login(username=username, password=password)

    def create_user(self, username, password):
        return User.objects.create_user(
            username=username,
            password=password,
        )

    def setUp(self):
        self.user_auth('liezl_agent', 'golden2022')
