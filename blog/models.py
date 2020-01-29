from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models


class Post(models.Model):
    message = models.TextField(blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(upload_to='posts/%Y/%m/%d', blank=True)
    description = models.CharField(verbose_name='image description', max_length=400, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} - {} - {}'.format(self.author.username, self.message, self.image)

    def clean(self):
        if not (self.message or self.image):
            raise ValidationError("You must specify either text or image")


class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} - {}'.format(self.author.username, self.text[:10])
