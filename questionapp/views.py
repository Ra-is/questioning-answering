from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.


class HelloApiView(APIView):
    """Test API View"""
    
    def get(self, request, format=None):
        """Return a list of APIView features"""
        an_apiview = [
            'Users HTTP methods ad function (get, post, put, patch, delete) and variable'
        ]
        return Response({'message':'Hello','an_apiview':an_apiview})