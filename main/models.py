from django.db import models
from django.contrib.auth.models import User


class About(models.Model):
    """
    A model for handling information about the website (or subject).
    """

    date_time = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    objects = models.Manager()

    def __str__(self) -> str:
        
        return self.description[:50]


class Blog(models.Model):
    """
    A model for handling blog posts only from the admin.
    """

    publisher = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=100, unique=True)
    subtitle = models.CharField(max_length=100)
    body = models.TextField()
    conclusion = models.TextField()
    sources = models.TextField(null=True)
    published = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self) -> str:
        
        return self.title


class File(models.Model):
    """
    A model for handling files.
    """

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    link = models.URLField()
    published = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self) -> str:
        
        return self.name
