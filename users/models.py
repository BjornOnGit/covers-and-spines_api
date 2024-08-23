from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager
from django.utils import timezone

class CustomUser(AbstractUser):
   username = models.CharField(max_length=100, unique=True)
   email = models.EmailField(max_length=100, unique=True)
   is_author = models.BooleanField(default=False)

   REQUIRED_FIELDS = ['email']
   USERNAME_FIELD = 'username'

   objects = CustomUserManager()
   
def __str__(self):
     self.username

class PasswordReset(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    token = models.CharField(max_length=100)
    expiration = models.DateTimeField()

    def __str__(self):
        return self.user.username
    
    def is_expired(self):
        return self.expiration < timezone.now()


# class CustomAdminLog(models.Model):
#     action_time = models.DateTimeField(auto_now_add=True)
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     content_type = models.ForeignKey('contenttypes.ContentType', on_delete=models.CASCADE)
#     object_id = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.PositiveSmallIntegerField()
#     change_message = models.TextField(blank=True, null=True)