from django.db import models
from . import models
from rest_framework import serializers


class userS(serializers.ModelSerializer):
    class meta:
        model = user
        fields  = ['username','email','psswd']