from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(username=email, password=password)
        if user:
            return Response({"message": "Inicio de sesión exitoso", "role": user.role}, status=status.HTTP_200_OK)
        return Response({"error": "Datos inválidos"}, status=status.HTTP_401_UNAUTHORIZED)