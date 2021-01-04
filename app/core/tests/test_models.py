from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.
class ModelTests(TestCase):

    def test_create_user_with_email_successfully(self):
        ''' test that creating a new user with an email is successful'''
        email = 'test@londonappdev.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        