from django.urls import path
from rest_framework.routers import DefaultRouter
from .apiviews import Tweet_viewset

routa = DefaultRouter()
routa.register('tweets',Tweet_viewset,base_name = 'api/v1')

urlpatterns = [

]

urlpatterns = urlpatterns + routa.urls
