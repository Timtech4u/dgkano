from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    time = models.DateTimeField()

    def __str__(self):
        return self.title
    