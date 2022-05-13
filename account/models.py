from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    work = models.CharField('Место работы', max_length=200)
    age = models.IntegerField('Возраст', null=True)
    images = models.ImageField('Аватарка', default='')

    def __str__(self):
        return self.user.username
