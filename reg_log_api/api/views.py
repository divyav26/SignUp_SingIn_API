from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import registerSerializer
from django.contrib.auth import authenticate, login
# Create your views here.

class SignUpAPIView(APIView):
    def get(self, request):
        return Response({'message':'This is get method'}, status=status.HTTP_200_OK)

    def post(self, request):
        try:
            obj = registerSerializer(data=request.data)
            if obj.is_valid():
                obj.save()
                return Response({'message':'Successfully Register'}, status=status.HTTP_201_CREATED)
            return Response(obj.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({'message':'Something is failed!!! due to {}'.format(str(e))},status=status.HTTP_400_BAD_REQUEST)

class LoginAPI(APIView):
    def post(self, request):
        username =request.data.get('username', None)
        password = request.data.get('password',None)

        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return Response({'message':'Logged In!!'}, status=status.HTTP_200_OK)
        else:
            return Response({'message':'Invalid Username And Password!!'} ,status=status.HTTP_400_BAD_REQUEST)

