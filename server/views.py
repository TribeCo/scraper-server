from rest_framework.views import APIView
from temsah import Temsah
from rest_framework.response import Response
from .serializers import *
from rest_framework import status
import requests
#---------------------------
class ScraperAPIView(APIView):
    """Scrape with proxy server"""
    def post(self, request):
        serializer = ScraperSerializer(data=request.data)
        if serializer.is_valid():
            scraper = Temsah(serializer.validated_data['url'])
            product = scraper.scrape()
            print(request.META)
            url_obj = Urls(applicant_site= request.META.get('HTTP_REFERER'), url= serializer.validated_data['url'])
            url_obj.save()
            
            return Response({'message': 'scraper returned.', 'data': product.convert_to_dictionary()})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#---------------------------
class ClientAPIView(APIView):
    """Clinet send request"""
    def post(self, request):
        url = 'http://localhost:8000/server/scraper/'
        data = {"url": request.data.get('url'),}

        response = requests.post(url, data=data)

        return Response({ 'data': response.json(),})       
#---------------------------

