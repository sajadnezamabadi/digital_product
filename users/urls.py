from django.urls import path 

from .views import *


urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("get-token/", GetTokenView.as_view(), name="get-token"),
]
