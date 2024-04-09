from django.urls import path
from .views import * 

urlpatterns = [
    path('scraper/', ScraperAPIView.as_view(),name="scraper"),
    path('clinet/', ClientAPIView.as_view(),name="clinet"),
    path('currency/', CurrencyAPIView.as_view(), name='currency'),
]