from django.db import models

# Create your models here.
from django.db import models

class Post(models.Model):
    first_name = models.CharField(max_length=30,null=True)
    last_name = models.CharField(max_length=30,null=True)
    def __str__(self):
          return f"{self.first_name}"

