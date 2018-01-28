from django.db import models

class User(models.Model):
    Name = models.CharField(max_length=250)
    Phone_no = models.IntegerField()

    def __str__(self):
        return self.Name



