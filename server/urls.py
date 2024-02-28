from django.urls import path
from .views import * 

urlpatterns = [
    path('scraper/', ScraperAPIView.as_view(),name="scraper"),
]