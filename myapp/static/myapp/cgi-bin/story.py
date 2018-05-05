from django.db import models

class Story(models.Model):
    comment = models.TextField()
