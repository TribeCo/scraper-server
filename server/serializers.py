from rest_framework import serializers
from .models import *
#---------------------------
class ScraperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Urls
        fields = '__all__'
#---------------------------