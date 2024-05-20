from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes,authentication_classes

from rest_framework.permissions import IsAuthenticated
from account.models import User
from account.serializers import CustomTokenObtainPairSerializer, UserSerializer
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


#     # Set the JWT token in an HTTP-only cookie (adjust cookie attributes as needed)
#     response.set_cookie(key='jwt', value=token, httponly=True,expires=payload['exp'].strftime('%a, %d %b %Y %H:%M:%S GMT'), samesite='strict')  

# Custom Login
@api_view(['POST'])
def login(request):

    serializer = CustomTokenObtainPairSerializer(data = request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.user
    tokens = serializer.validated_data
    # Get additional user information

    if user.is_superuser == True:

        user_info = {
            'userID': user.UserID,
            'firstname': user.first_name,
            'role':'Admin'
        }
        # Add user information to the response data
        response_data = {
            'refresh': tokens['refresh'],
            'access': tokens['access'],
            'user_info':user_info
        }
        return Response(response_data, status=200)
    elif user.is_staff == True:
        user_info = {
            'userID': user.UserID,
            'firstname': user.first_name,
            'role':'Staff'
        }
        
        response_data = {
            'refresh': tokens['refresh'],
            'access': tokens['access'],
            'user_info':user_info
        }
        return Response(response_data, status=200)
    else:
        user_info = {
            'userID': user.UserID,
            'firstname': user.first_name,
            'role':'Student'
        }
        
        response_data = {
            'refresh': tokens['refresh'],
            'access': tokens['access'],
            'user_info':user_info
        }
        return Response(response_data, status=200)


# @api_view(['POST'])
# def logout(request):
#     response = Response()
#     auth.logout(request)
#     response.delete_cookie('jwt')
#     response.data = {
#         'message':"Logged Out"
#     }
#     return response

