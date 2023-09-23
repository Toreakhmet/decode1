from django.db import models
from django.contrib.auth.models import AbstractUser


class tovars(models.Model):
    name = models.CharField(max_length=122)
    description = models.TextField()
    price = models.IntegerField()
    data_add = models.DateTimeField(auto_now_add=True)  # Исправлено auto_add на auto_now_add
    image=models.ImageField(upload_to='images_tovar/')

# Create your models here.
class CustomUser(AbstractUser):
    messages = models.TextField(default='', blank=True)

    image=models.ImageField(("photo"), upload_to='images/', height_field=None, width_field=None, max_length=None)