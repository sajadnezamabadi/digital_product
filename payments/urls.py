from django.urls import path

from .views import *


########################

urlpatterns = [
    path("gateways/", GatewayViews.as_view()),
    path("pay/", PaymentsView.as_view()),
]
