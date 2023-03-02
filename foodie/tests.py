from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.
class Users_model_Test(TestCase):
    def setUp(self):
        User.objects.create(username="testUser")
    
    def test_user_exists(self):
        testUser = User.objects.get(username="testUser")

