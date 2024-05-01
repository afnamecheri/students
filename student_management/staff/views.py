from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from django.contrib.auth import authenticate
from .models import Token

@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        
  
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        Token.objects.create(user=user, access_token=access_token, refresh_token=refresh_token)

        return Response({
            "user": serializer.data,
            "access_token": access_token
        }, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

User

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Token
from rest_framework_simplejwt.tokens import AccessToken

@api_view(['POST'])
def signup(request):
    username = request.data.get("username")
    password = request.data.get("password")
    email = request.data.get("email")

    user = User.objects.create_user(username=username, password=password, email=email)

    if user:
        
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        Token.objects.create(user=user, access_token=access_token, refresh_token=refresh_token)

        return Response({"message": "User registered successfully", "access_token": access_token}, status=status.HTTP_201_CREATED)
    else:
        return Response({"error": "Failed to register user"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def userlogin(request):
    print(request.data)
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)

    if user:
  
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)

            return Response({
                'username': username,
                'password': password,
                'access_token': access_token,
                'refresh_token':refresh_token
            }, status=status.HTTP_200_OK)
        
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)



@api_view(['POST'])
def userlogout(request):
    try:
        authorization_header = request.headers.get('Authorization')
        if authorization_header and authorization_header.startswith('Bearer '):
            access_token = authorization_header.split(' ')[1]

            token = AccessToken(access_token)
            token.blacklist()

            return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid authorization header"}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)