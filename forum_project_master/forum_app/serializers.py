from django.db import models
from . import models
from rest_framework import serializers
class userS(serializers.ModelSerializer):
    class meta:
        model = models.users
        fields  = ['id',
                   'username',
                   'email',
                   'psswd'
                   ]
class postS(serializers.ModelSerializer):
    class meta:
        model=models.post
        fields=['id',
                  'title',
                  'content',
                  'post_category',
                  'hour_post'
                  ]
class category(serializers.ModelSerializer):
    class meta:
        model=models.category
        fields=['id',
                'ct_name']