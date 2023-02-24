from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.db import models
from PIL import Image


class Ticket(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=2048, blank=True)
    image = models.ImageField(null=True, blank=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True
    )
    IMAGE_MAX_SIZE = (150, 193)
    time_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.title}"

    def resize_image(self):
        image = Image.open(self.image)
        image.thumbnail(self.IMAGE_MAX_SIZE)
        image.save(self.image.path)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.resize_image()


class Review(models.Model):
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
    headline = models.CharField(max_length=128)
    rating = models.PositiveSmallIntegerField(
        # validates that rating must be between 0 and 5
        validators=[MinValueValidator(0), MaxValueValidator(5)],
    )
    body = models.CharField(max_length=8192, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.headline}"
