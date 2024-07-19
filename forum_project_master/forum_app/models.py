from django.db import models
import datetime as dt

# Create your models here.


class category(models.Model):
    ct_name=models.CharField(max_length=80)
    id=models.UUIDField().primary_key=True

class users(models.Model):
    username = models.CharField(max_length=20)
    email= models.EmailField()
    psswd=models.CharField(max_length=12)

class post_structure(models.Model):
    title=models.CharField(max_length=150)
    content=models.CharField(max_length=600)
    post_category=category.id
    hour_post = dt.datetime.now()
    author=users.username
