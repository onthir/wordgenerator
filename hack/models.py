from django.db import models

# Create your models here.
class Dictionary(models.Model):
    word = models.CharField(max_length=500)

    def __str__(self):
        return self.word