from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from . models import Program, Student, Todos, User
from . serializers import ProgramSerializer, StudentSerializer ,TodosSerializer, UserSerializer
from rest_framework.exceptions import AuthenticationFailed
import jwt,datetime
# Create your views here.

def hellomsg(request):
    return HttpResponse( "Hello from backend")

@api_view(['GET', 'POST'])
def example_view(request):
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
    

# LOGIN
# pip install PyJWT
@api_view(['POST'])
def login(request):
    email = request.data['email']
    password = request.data['password']
    user = User.objects.filter(email = email).first()

    if user is None:
        raise AuthenticationFailed("User does not exist")
    if not user.check_password(password):
        raise AuthenticationFailed('Incorrect password')
    
    payload = {
        'id': user.UserID,
        'exp': datetime.datetime.now() + datetime.timedelta(minutes=1),
        'iat' :datetime.datetime.now()
    }

    response = Response()

    token = jwt.encode(payload, 'secret_key', algorithm='HS256')
    
    response.set_cookie(key='jwt', value = token, httponly=True)
    
    return response


# GET AUTHENTICATED USER
@api_view(['GET'])
def getautUser(request):
    token = request.COOKIES.get('jwt')
    if not token:
        raise AuthenticationFailed('UnAuthenticated')
    # try:
    #     payload = jwt.decode(token, 'secret', algorithms=['HS256'])

    # # except jwt.ExpiredSignatureError:
    # #     raise AuthenticationFailed('UnAuthenticated, signature expired')
    # user = User.objects.filter(id = payload['id']).first()
    # serializer = UserSerializer(user)
    return Response({token,1})

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
def register_student(request):
    
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        # Create a user with a hashed password
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


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

