from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .models import CustomToken 
from django.contrib.auth.models import User
from rest_framework import status



class RegisterView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
     
    
        if not username or not password:
            return Response({"error": "Username and Password are required"}, status=status.HTTP_400_BAD_REQUEST)

      
        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)

       
        user = User.objects.create_user(username=username, password=password, )
        user.save()

        return Response({
            "message": "User registered successfully!",
            "username": user.username
        }, status=status.HTTP_201_CREATED)
    

class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user_origin = request.data.get("origin") 

       
        user = authenticate(username=username, password=password)

        if user:
            
            token, created = CustomToken.objects.get_or_create(user=user)

          
            token.origin = user_origin 
            token.save()

            return Response({
                "token": token.key,
                "origin": token.origin,
                "message": "Login Successful!"
            })
        else:
            return Response({"error": "Wrong Credentials"}, status=400)