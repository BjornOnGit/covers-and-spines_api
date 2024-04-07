from django.conf import settings
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    documents = models.FileField(upload_to='documents/', null=True, blank=True)
    cover = models.ImageField(upload_to='covers/')

    def __str__(self):
        return self.title

# Create your models here.
