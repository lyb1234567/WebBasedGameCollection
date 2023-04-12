from django.test import TestCase
from django.test import TestCase
from django.utils import timezone
from customUser.models import User
from GamePublisher.models import GamePublisher
from .models import Review

class ReviewModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword',
            firstName='Test',
            lastName='User',
            profilePic=None,
            userInfo='Test user for testing purposes.',
            dateOfBirth=timezone.now().date(),
            userType='Player',
            location='Test City'
        )
        self.publisher = GamePublisher.objects.create(
            pubPassword="ComplexP@ssw0rd!",
            pubEmail="publisher@example.com",
            publisherDescription="Test publisher description",
            publisherInfo="Test publisher info",
        )
    def test_create_review(self):
        review = Review.objects.create(
            reviewCode="R0001",
            user=self.user,
            publisher=self.publisher,
            rate=4,
            content="This is a test review.",
            status="Published"
        )
        self.assertEqual(review.reviewCode, "R0001")
        self.assertEqual(review.user, self.user)
        self.assertEqual(review.publisher, self.publisher)
        self.assertEqual(review.rate, 4)
        self.assertEqual(review.content, "This is a test review.")
        self.assertEqual(review.status, "Published")

    def test_update_review(self):
        review = Review.objects.create(
            reviewCode="R0001",
            user=self.user,
            publisher=self.publisher,
            rate=4,
            content="This is a test review.",
            status="Published"
        )
        Review.objects.update_review("R0001", rate=5, content="This is an updated review.")
        updated_review = Review.objects.get(reviewCode="R0001")
        self.assertEqual(updated_review.rate, 5)
        self.assertEqual(updated_review.content, "This is an updated review.")

    def test_delete_review(self):
        review = Review.objects.create(
            reviewCode="R0001",
            user=self.user,
            publisher=self.publisher,
            rate=4,
            content="This is a test review.",
            status="Published"
        )
        Review.objects.delete_review("R0001")
        with self.assertRaises(Review.DoesNotExist):
            Review.objects.get(reviewCode="R0001")

