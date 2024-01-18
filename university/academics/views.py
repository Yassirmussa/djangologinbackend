from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes,authentication_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from rest_framework.permissions import AllowAny, IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly
from . models import Program, Student, Todos
from . serializers import ProgramSerializer, StudentSerializer ,TodosSerializer
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
    

@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def example_view(request, format=None):
    content = {
        'user': str(request.user),  # `django.contrib.auth.User` instance.
        'auth': str(request.auth),  # None
    }
    return Response(content)



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
@permission_classes([IsAuthenticated])
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

