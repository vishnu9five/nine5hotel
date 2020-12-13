from django.db import models

# Create your models here.
class suits(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    img = models.ImageField(upload_to='imgs')
    price = models.IntegerField(10)
    offer = models.BooleanField(default=False)
    