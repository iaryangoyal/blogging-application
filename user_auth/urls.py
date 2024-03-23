from django.urls import path,include
from .views import *
urlpatterns = [
    path('register/', UserLoginApiView.as_view()),
    path('login/', UserLoginAPIView.as_view(), name='login'),
]