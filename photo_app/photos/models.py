from django.db import models
from django.contrib.auth.models import User

class Photo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    image = models.ImageField(upload_to='photos/')
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name