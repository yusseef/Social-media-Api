
from django.urls import path, include
from .views import *
urlpatterns = [
    path('', UserView.as_view(), name = 'user' ), 
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
   
]
