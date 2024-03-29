from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes,authentication_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from rest_framework.permissions import AllowAny, IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly
from . models import Course, Program, Student, Todos
from . serializers import CourseSerializer, ProgramSerializer, StudentSerializer ,TodosSerializer
# Create your views here.

def hellomsg(request):
    return HttpResponse( "Hello from academics backend")

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
@permission_classes([IsAuthenticated])
def insertStudent(request):
    # Extract the user from request
    user = request.user
    studentData = {'UserID':user.UserID}
    print(studentData['UserID'])
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
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


# HANDLING COURSE
# ADD COURSE
@api_view(['POST'])
def insertCourse(request):
    serializer = CourseSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

# GET ALL COURSES
@api_view(['GET'])
def getCourse(request):
    course = Course.objects.all()
    serializer = CourseSerializer(course, many=True)
    return Response(serializer.data, status=200)

# GET COURSE BY ID
@api_view(['GET'])
def getCourseByID(request, CoID):
    try:
        course = Course.objects.get(CoID = CoID)
        serializer = CourseSerializer(course)
        return Response(serializer.data, status=200)
    except:
        return Response (f' Course with ID {CoID} does not exist')
    

# UPDATE COURSE
@api_view(['PUT'])
def updateCourse(request, CoID):
    try:
        course = Course.objects.get(CoID = CoID)
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    except:
        return Response (f' Course with ID {CoID} does not exist')


# DELETE COURSE   
@api_view(['DELETE'])
def deleteCourse(request, CoID):
    try:
        course = Course.objects.get(CoID = CoID)
        course.delete()
        return Response(f'Course with ID {CoID} deleted successifully')
    except:
        return Response (f' Course with ID {CoID} does not exist')
    
# GET COURESES FALL IN THE SAME PROGRAM
@api_view(['GET'])
def getCourseByProID(request, ProID):
    # try:
        course = Course.objects.filter(ProID_id = ProID)
        if (len(course)>0):
            serializer = CourseSerializer(course, many=True)
            return Response(serializer.data, status=200)
        else:
            return Response(f'Program with ID {ProID} has no any course')
    # except:
    #     return Response(f'Program with ID {ProID} has no any course')