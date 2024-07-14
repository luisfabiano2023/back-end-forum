from django.db import models
import date,datetime as dt

# Create your models here.

class users:
    username = models.CharField()
    email= models.EmailField()
    psswd=models.CharField()
class post_structure:
    title=models.CharField(max_length=150)
    content=models.CharField(max_length=600)
    post_category=self.category.id
    hour_post = dt.datetime.now()
    
    def __str__(self) -> str:
        pass


class category:
    ct_name=models.CharField(max_length=80)
    id=models.UUIDField()

