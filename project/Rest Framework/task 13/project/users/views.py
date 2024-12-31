from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import UserSerializer
from django.contrib.auth.models import User

class RegisterView(APIView):
    """ View for user registration """
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProtectedView(APIView):
    """ View for a protected endpoint """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'message': 'You have accessed a protected endpoint!'})
