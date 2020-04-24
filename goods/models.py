from django.db import models


# Create your models here.
class Goods(models.Model):
    name = models.CharField(max_length=20)
    price = models.TextField()
    img = models.ImageField()
    content = models.TextField()
    num = models.IntegerField()
