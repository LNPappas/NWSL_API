from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(email='test@nwslfantasy.com', password='testpass'):
    '''Create a sample user'''
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_email_successfully(self):
        '''test that creating a new user with an email is successful'''
        email = 'test@nwslfantasy.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        '''test email for new user is normalized'''
        email = 'test@nwslfantasy.com'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        '''test if new user email is invalid an error is raised'''
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        '''test creating a new superuser'''
        user = get_user_model().objects.create_superuser(
            'test@nwslfantasy.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        '''Test the tag string representation'''
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Forward'
        )

        self.assertEqual(str(tag), tag.name)
