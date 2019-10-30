from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with and email is successfull"""
        email = 'test@email.ru'
        password = 'qwerty1234'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test that email of a new user is normalized"""
        email = 'my_test@UPPERCASE.RU'
        user = get_user_model().objects.create_user(email, 'test1234')
        self.assertEqual(user.email, email.lower())

    def test_new_user_email_validation(self):
        """Test that a new user with empty email can't be registered"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '1234test')
