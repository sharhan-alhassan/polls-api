

from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    # Magically turn the Todo Model into Json for 
    # our endpoint to be collected by the frontend
    class Meta:
        model = Todo
        fields = ('id', 'title', 'body',)