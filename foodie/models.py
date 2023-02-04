from django.db import models

# Create your models here.
class Users(models.Model):
    Username = models.CharField(max_length=100)

    def __str__(self):
        return self.Username