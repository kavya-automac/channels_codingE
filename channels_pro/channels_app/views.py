from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from.serializers import *
from . models import *

class TestApi(APIView):
    def post(self,request):
        serializer=TestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'success'})
    def get(self,request):
        data=Test.objects.all()
        serializer=TestSerializer(data,many=True)
        return Response(serializer.data)