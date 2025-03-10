from django.db import models

class Language(models.Model):
    name = models.CharField(max_length=100, unique=True)
    flag = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name