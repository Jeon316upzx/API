from .models import Tweet
from rest_framework import viewsets
from .serializers import Tweet_serializer

class Tweet_viewset(viewsets.ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = Tweet_serializer
