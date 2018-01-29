from django.db import models
from django.core.urlresolvers import reverse

class User(models.Model):
    Name = models.CharField(max_length=250)
    Phone_no = models.IntegerField()

    def get_absolute_url(self):
        return reverse('users:index')

    def __str__(self):
        return self.Name
