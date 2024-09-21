from django.urls import path

from .views import *


########################

urlpatterns = [
    path("packages/", PackageView.as_view()),
    path("subscription/", SubscriptionView.as_view()),
]
