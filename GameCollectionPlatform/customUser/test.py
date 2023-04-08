from django.test import TestCase
from customUser.models import User

class CustomUserTests(TestCase):

    def setUp(self):
        self.username = 'testuser'
        self.email = 'test@example.com'
        self.password = 'testpassword'

    def test_create_user(self):
        user = User.objects.create_user(
            username=self.username,
            email=self.email,
            password=self.password,
            firstName='John',
            lastName='Doe',
            userType='Player',
            profilePic=None,
            userInfo='Test User',
            dateOfBirth='2000-01-01',
            location='Example City'
        )
        self.assertIsNotNone(user)
        self.assertEqual(user.username, self.username)
        self.assertEqual(user.email, self.email)

    def test_create_superuser(self):
        user = User.objects.create_superuser(
            username=self.username,
            email=self.email,
            password=self.password
        )
        self.assertIsNotNone(user)
        self.assertEqual(user.username, self.username)
        self.assertEqual(user.email, self.email)
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_update_user(self):
        user = User.objects.create_user(
            username=self.username,
            email=self.email,
            password=self.password,
            firstName='John',
            lastName='Doe',
            userType='Player',
            profilePic=None,
            userInfo='Test User',
            dateOfBirth='2000-01-01',
            location='Example City'
        )
        user.firstName = 'Updated'
        user.lastName = 'Name'
        user.save()

        updated_user = User.objects.get(username=self.username)
        self.assertEqual(updated_user.firstName, 'Updated')
        self.assertEqual(updated_user.lastName, 'Name')

    def test_delete_user(self):
        user = User.objects.create_user(
            username=self.username,
            email=self.email,
            password=self.password,
            firstName='John',
            lastName='Doe',
            userType='Player',
            profilePic=None,
            userInfo='Test User',
            dateOfBirth='2000-01-01',
            location='Example City'
        )
        user.delete()

        with self.assertRaises(User.DoesNotExist):
            User.objects.get(username=self.username)
