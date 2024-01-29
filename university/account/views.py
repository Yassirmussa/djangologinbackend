from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes,authentication_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from account.models import User
from account.serializers import UserSerializer
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import auth
import jwt,datetime
# Create your views here.

def msg(request):
    return Response('Hello from accountApp')

# HANDLING USER
# insert
@api_view(['POST'])
def insertUser(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


# get all
@api_view(['GET'])
def getUser(request):
    user = User.objects.all()
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data, status=200)



# get by ID
@api_view(['GET'])
def getUserByID(request, UserID):
    try:
        user = User.objects.get(UserID = UserID)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=200)
    except:
        return Response(f"User with ID {UserID} does not exist")



# update user 

@api_view(['PUT'])
def updateUser(request, UserID):
    try:
        user = User.objects.get(UserID = UserID)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    except:
        return Response(f"User with ID {UserID} does not exist")
    
# delete user

@api_view(['DELETE'])
def deleteUser(request, UserID):
    try:
        user = User.objects.get(UserID = UserID)
        user.delete()
        return Response(f"User with ID {UserID} deleted successifully")
    except:
        return Response(f"User with ID {UserID} does not exist")


# pip install PyJWT
@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    
    if not email or not password:
        raise AuthenticationFailed('Email and password are required.')

    user = User.objects.filter(email=email).first()

    if user is None or not user.check_password(password):
        raise AuthenticationFailed('Invalid credentials.')

    # Define the payload for the JWT token
    payload = {
        'id': user.UserID,  
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),  # Token expiration time 
        'iat': datetime.datetime.utcnow(),
    }

    # Generate the JWT token
    token = jwt.encode(payload, 'YOUR_SECRET_KEY_HERE', algorithm='HS256')

    # Create a response
    response = Response()

    # Set the JWT token in an HTTP-only cookie (adjust cookie attributes as needed)
    response.set_cookie(key='jwt', value=token, httponly=True,expires=payload['exp'].strftime('%a, %d %b %Y %H:%M:%S GMT'), samesite='strict')  
    
    # auth.login(request, user)
    # Update the last_login timestamp for the user
    user.last_login = datetime.datetime.utcnow()
    user.save(update_fields=['last_login'])

    response.data = {
        'message':"Login success"
    }
    # Return the response
    return response


# GET AUTHENTICATED USER
@api_view(['GET'])
def getauthUser(request):
    token = request.COOKIES.get('jwt')
    
    if not token:
        raise AuthenticationFailed('Unauthenticated: No token provided.')

    try:
        payload = jwt.decode(token, 'YOUR_SECRET_KEY_HERE', algorithms=['HS256'])
        
        # Retrieve user based on the user ID from the token payload
        user = User.objects.filter(UserID=payload['id']).first()

        if user is None:
            raise AuthenticationFailed('User not found.')
        
        # Serialize the user object
        serializer = UserSerializer(user)
        
        # Return the serialized user data as a response
        return Response(serializer.data)
    
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthenticated: Token signature has expired.')
    
    except jwt.InvalidTokenError:
        raise AuthenticationFailed('Unauthenticated: Invalid token.')

@api_view(['POST'])
def logout(request):
    response = Response()
    # auth.logout(request)
    response.delete_cookie('jwt')
    response.data = {
        'message':"Logged Out"
    }
    return response

