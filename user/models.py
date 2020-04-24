from django.db import models
from django.contrib.auth.hashers import make_password


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=18)
    password = models.CharField(max_length=200)
    phone = models.IntegerField()
    address = models.TextField()

    def save(self, *args, **kwargs):
        if not self.password.startswith('pbkdf2_sha256'):
            self.password = make_password(self.password)
        super(User, self).save(*args, **kwargs)
