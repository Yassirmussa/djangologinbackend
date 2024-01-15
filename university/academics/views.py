from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes,authentication_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from . models import Program, Student, Todos, User
from . serializers import ProgramSerializer, StudentSerializer ,TodosSerializer, UserSerializer
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import auth 
import jwt,datetime
# Create your views here.

def hellomsg(request):
    return HttpResponse( "Hello from backend")

@api_view(['GET', 'POST'])
def two_request(request):
    if request.method == 'GET':
        data = {'message': 'This is a GET request'}
        return Response(data)
    elif request.method == 'POST':
        # Process the POST data
        data = {'message': 'This is a POST request'}
        return Response(data)
    

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



@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def example_view(request, format=None):
    content = {
        'user': str(request.user),  # `django.contrib.auth.User` instance.
        'auth': str(request.auth),  # None
    }
    return Response(content)

# LOGIN
# pip install PyJWT
# @api_view(['POST'])
# def login(request):
#     email = request.data['email']
#     password = request.data['password']
#     user = User.objects.filter(email = email).first()

#     if user is None:
#         raise AuthenticationFailed("User does not exist")
#     if not user.check_password(password):
#         raise AuthenticationFailed('Incorrect password')
#     auth.login(request, user)
#     payload = {
#         'id': user.UserID,
#         'exp': datetime.datetime.now() + datetime.timedelta(minutes=1),
#         'iat' :datetime.datetime.now()
#     }

#     response = Response()

#     token = jwt.encode(payload, 'secret', algorithm='HS256')
    
#     response.set_cookie(key='jwt', value=token, httponly=True)
    
#     return response


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
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1),  # Token expiration time (adjust as needed)
        'iat': datetime.datetime.utcnow(),
    }

    # Generate the JWT token
    token = jwt.encode(payload, 'YOUR_SECRET_KEY_HERE', algorithm='HS256')

    # Create a response
    response = Response()

    # Set the JWT token in an HTTP-only cookie (adjust cookie attributes as needed)
    response.set_cookie(key='jwt', value=token, httponly=True, samesite='strict')  
    
    # auth.login(request, user)
    # Update the last_login timestamp for the user
    user.last_login = datetime.datetime.now()
    user.save(update_fields=['last_login'])


    # Return the response
    return response

# GET AUTHENTICATED USER
@api_view(['GET'])
def getautUser(request):
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
    response.delete_cookie('jwt')
    response.data = {
        'message':"Logged Out"
    }
    return response

#insert program
@api_view(['POST'])
def insertProgram(request):
   seriliazer = ProgramSerializer(data=request.data)
   if seriliazer.is_valid():
       seriliazer.save()
       return Response(seriliazer.data, status=201)
   return Response(seriliazer.errors, status=400) 

#get all programs
@api_view(['GET'])
def getProgram(request):
    program = Program.objects.all()
    serializer = ProgramSerializer(program, many=True)
    return Response(serializer.data)

#get program by id
@api_view(['GET'])
def getProgramByID(request, ProID):
    try:
        program = Program.objects.get(ProID = ProID)
        serializer = ProgramSerializer(program)
        return Response(serializer.data, status=200)
    except:
        return Response(f'Program with ID {ProID} does not exist')
    
#update program
@api_view(['PUT'])
def updateProgram(request, ProID):
    try:
        program = Program.objects.get(ProID = ProID)
        serializer = ProgramSerializer(program, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(f'Program with ID {ProID} updated successiful')
    except:
        return Response(f'Program with ID {ProID} does not exist')

#delete progam
@api_view(['DELETE'])
def deleteProgram(request, ProID):
    try:
        program = Program.objects.get(ProID = ProID)
        program.delete()
        return Response(f'Program with ID {ProID} deleted successiful')
    except:
        return Response(f'Program with ID {ProID} does not exist')
    


#handle Todos

@api_view(['POST'])
def insertTodo(request):
    serializer = TodosSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response (serializer.errors, status=400)

@api_view(['GET'])
def getTodos(request):
    todos = Todos.objects.all()
    seriallizer = TodosSerializer(todos, many=True)
    return Response(seriallizer.data, status=200)

@api_view(['GET'])
def getTodoById(request, id):
    try:
        todo = Todos.objects.get(id= id)
        serializer = TodosSerializer(todo)
        return Response(serializer.data, status=200)
    except:
        return Response(f' Todo with ID {id} does not exist')

@api_view(['PUT'])
def updateTodo(request, id):
    try:
        todo = Todos.objects.get(id = id)
        serializer = TodosSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    except:
        return Response(f' Todo with ID {id} does not exist')


@api_view(['DELETE'])
def deleteTodo(request, id):
    try:
        todo = Todos.objects.get(id = id)
        todo.delete()
        return Response(f' Todo with ID {id} deleted succesifully')
    except:
        return Response(f' Todo with ID {id} does not exist')



# manging student
@api_view(['POST'])
@permission_classes([AllowAny])  # Allow any user (no authentication required for registration)
def registerStudent(request):
    
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        # Create a user with a hashed password
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def getStudent(request):
    student = Student.objects.all()
    serializer = StudentSerializer(student, many=True)
    return Response(serializer.data, status=200)

@api_view(['PUT'])
def updateStudent(request, StuID):
    try:
        student = Student.objects.get(StuID = StuID)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    except:
        return Response(f' Todo with ID {StuID} does not exist')


@api_view(['DELETE'])
def deleteStudent(request, StuID):
    try:
        todo = Todos.objects.get(StuID = StuID)
        todo.delete()
        return Response(f' Student with ID {StuID} deleted succesifully')
    except:
        return Response(f' Student with ID {StuID} does not exist')

@api_view(['DELETE'])
def deleteAllStudent(request):
    student = Student.objects.all()
    student.delete()
    return Response(f'All student have deleted')

