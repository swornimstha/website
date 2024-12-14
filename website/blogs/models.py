from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """
    Model for my posts
    """
    title = models.CharField(max_length=20, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_on"]

    def get_absolute_url(self):
        """
        Returns the URL to access a particular instance of my post
        """
        return reverse("model-detail-view", args=[str(self.id)])

    def __str__(self):
        """
        String for representing post object(in the admin site)
        """
        return self.title
