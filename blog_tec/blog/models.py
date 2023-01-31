from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Post(models.Models):
   title = models.CharField(max_length=255)
   resumo = models.CharField(max_length=255)
   content = models.TextField()
   author = models.ForeignKey(User, on_delete=models.PROTECT)
