from rest_framework import serializers
from .models import Tweet

class Tweet_serializer(serializers.ModelSerializer):
    class Meta(object):
        model = Tweet
        fields = '__all__'
