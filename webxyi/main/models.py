from django.db import models

# Create your models here.

class Aga(models.Model):
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    history = models.TextField()
    content = models.TextField()
    invite = models.TextField()

    def __str__(self):
        return self.name