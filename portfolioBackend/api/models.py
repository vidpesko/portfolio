from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    highlighted = models.BooleanField(default=False)
    description = models.TextField()
