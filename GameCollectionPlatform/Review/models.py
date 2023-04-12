from django.db import models

class ReviewManager(models.Manager):
    def create(self, reviewCode, user, publisher, rate, content, status):
        review = self.model(
            reviewCode=reviewCode,
            user=user,
            publisher=publisher,
            rate=rate,
            content=content,
            status=status,
        )
        review.save()
        return review

    def update_review(self, reviewCode, **kwargs):
        review = self.get(reviewCode=reviewCode)
        for key, value in kwargs.items():
            setattr(review, key, value)
        review.save()
        return review

    def delete_review(self, reviewCode):
        review = self.get(reviewCode=reviewCode)
        review.delete()

# Create your models here.
class Review(models.Model):
    reviewCode = models.CharField(max_length=50, primary_key=True)
    user = models.ForeignKey("customUser.User", on_delete=models.CASCADE, null=True, blank=True)
    publisher = models.ForeignKey('GamePublisher.GamePublisher', on_delete=models.CASCADE, null=True, blank=True)
    rate = models.IntegerField()
    content = models.TextField()
    status = models.CharField(max_length=20)
    objects=ReviewManager()