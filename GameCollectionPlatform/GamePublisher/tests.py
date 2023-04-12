from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from GamePublisher.models import GamePublisher

class GamePublisherTests(TestCase):

    def setUp(self):
        self.pub_password = 'C0mplex!Password'
        self.pub_email = 'publisher@example.com'
        self.publisher_description = 'Example publisher'
        self.publisher_info = 'Additional information'

    def test_create_publisher(self):
        publisher = GamePublisher.objects.create(
            pubPassword=self.pub_password,
            pubEmail=self.pub_email,
            publisherDescription=self.publisher_description,
            publisherInfo=self.publisher_info
        )
        self.assertIsNotNone(publisher)
        self.assertEqual(publisher.pubEmail, self.pub_email)
        self.assertNotEqual(publisher.pubPassword, self.pub_password)  # Ensure the password is hashed

    def test_update_publisher(self):
        publisher = GamePublisher.objects.create(
            pubPassword=self.pub_password,
            pubEmail=self.pub_email,
            publisherDescription=self.publisher_description,
            publisherInfo=self.publisher_info
        )
        updated_description = 'Updated publisher description'
        publisher.publisherDescription = updated_description
        publisher.save()

        updated_publisher = GamePublisher.objects.get(pubEmail=self.pub_email)
        self.assertEqual(updated_publisher.publisherDescription, updated_description)
    def test_is_password_complex(self):
        # Test valid password
        valid_password = 'C0mplex!Password'
        self.assertTrue(GamePublisher.objects.is_password_complex(valid_password))

        # Test invalid passwords
        invalid_passwords = [
            'password',        # Too short, no uppercase, no digit, no special characters
            'ComplexPassword', # No digit, no special characters
            'c0mplexpassword', # No uppercase, no special characters
            'CompleX!assword',# No digit
            'C0mpleX1assword',
        ]

        for password in invalid_passwords:
            self.assertFalse(GamePublisher.objects.is_password_complex(password))

    def test_delete_publisher(self):
        publisher = GamePublisher.objects.create(
            pubPassword=self.pub_password,
            pubEmail=self.pub_email,
            publisherDescription=self.publisher_description,
            publisherInfo=self.publisher_info
        )
        publisher.delete()
        with self.assertRaises(GamePublisher.DoesNotExist):
            GamePublisher.objects.get(pubEmail=self.pub_email)
