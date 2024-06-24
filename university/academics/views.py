from urllib import response
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated

from academics.models import Allocation, Examiner, PostGraduateOfficer, Student,Research,Recommendation,Result, Supervisor
from academics.serializers import AllocationSerializer, ExaminerSerializer, PGOSerializer, StudentSerializer, ResearchSerializer, RecommendationsSerializer, ResultSerializer, SupervisorSerializer

# Handle Staff registration by Admin
# insert 
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def registerSupervisor(request):
    user = request.user
    if user.is_superuser:
        serializer = SupervisorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    return Response('You have not access to this operation')

# get All Supervisor
@api_view(['GET'])
def getAllSupervisor(request):
    supervisor = Supervisor.objects.all()
    serializer = SupervisorSerializer(supervisor, many=True)
    return Response(serializer.data, status=200)

# insert Examiner
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def registerExaminer(request):
    user = request.user
    if user.is_superuser:
        serializer = ExaminerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    return Response('You have not access to this operation')

# get All Examiner
@api_view(['GET'])
def getAllSupervisor(request):
    examiner = Examiner.objects.all()
    serializer = ExaminerSerializer(examiner, many=True)
    return Response(serializer.data, status=200)

# insert PGO
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def registerExaminer(request):
    user = request.user
    if user.is_superuser:
        serializer = PGOSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    return Response('You have not access to this operation')

# get All PGO
@api_view(['GET'])
def getAllPGO(request):
    pgo = PostGraduateOfficer.objects.all()
    serializer = ExaminerSerializer(pgo, many=True)
    return Response(serializer.data, status=200)

# register Student
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def registerStudent(request):
    user = request.user
    request.data ['UserID'] = user.UserID
    if not user.is_superuser and not user.is_staff:
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    return Response('You have not access to this operation')

@api_view(['GET'])
def getAllStudent(request):
    student = Student.objects.all()
    serializer = StudentSerializer(student, many=True)
    return Response(serializer.data, status=200)

# send Research
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def sendResearch(request):
    user = request.user
    try:
        student  = Student.objects.get(UserID = user.UserID)
        request.data ['StuID'] = student.StuID
        if not user.is_superuser and not user.is_staff:
            serializer = ResearchSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        return Response('You have not access to this operation')
    except Student.DoesNotExist:
        return Response({'error': 'Student not found for this user'}, status=404)

@api_view(['GET'])
def getAllResearch(request):
    user = request.user
    if user.is_supervisor:
        try:
            supervisor = Supervisor.objects.get(UserID = user.UserID)
            # print(user.UserID)
            # print(supervisor)
            # print(supervisor.SupID)
            allocation = Allocation.objects.get(SupID = supervisor.SupID)
    
            # print(allocation.StuID.StuID)
            student = Student.objects.get(StuID = allocation.StuID.StuID)
            # print(student.StuID)
            research = Research.objects.filter(StuID = student.StuID)
            serializer = ResearchSerializer(research, many=True)
            return Response(serializer.data, status=200)
        except:
             return Response('Access Denied!!!, You have not allocated any student')
    elif user.is_examiner:
        examiner = Examiner.objects.get(UserID = user.UserID)

        allocation = Allocation.objects.get(ExID = examiner.ExID)
        # print(allocation.ExID.ExID)
        student = Student.objects.get(StuID = allocation.StuID.StuID)
        # print(allocation.StuID.StuID)
        getResearch = Research.objects.get(StuID = student.StuID)
        
        if getResearch.Status == 'completed':

            research = Research.objects.filter(StuID = student.StuID)
            serializer = ResearchSerializer(research, many=True)
            return Response(serializer.data, status=200)
        else:
            return Response('Sorry! No research completed at Supervisor level')
    elif user.is_PGO:
        research = Research.objects.all()
        serializer = ResearchSerializer(research, many=True)
        return Response(serializer.data, status=200)

    else:
        try:
            student = Student.objects.get(UserID = user.UserID)
            research = Research.objects.get(StuID = student.StuID)
            serializer = ResearchSerializer(research)
            return Response(serializer.data, status=200)
        except Research.DoesNotExist:
            return Response('You have not sent your research!!! can you send it now?')

# send Recommendation
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def sendRecommendation(request):
    user = request.user
    if user.is_supervisor:
        try:
            supervisor = Supervisor.objects.get(UserID = user.UserID)
            # print(supervisor)
            allocation = Allocation.objects.get(SupID = supervisor.SupID)
            # print(allocation)
            student = Student.objects.get(StuID = allocation.StuID.StuID)
            # print(student)    
            research = Research.objects.filter(StuID = student.StuID)
            # print(research)
            
            serializer = RecommendationsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
            return Response('Well responded')
        except:
            return Response('Access denied!!! No sudent allocated')
    return Response('You have not access to this operation')

@api_view(['GET'])
def getAllRecommendation(request):
    user = request.user
    try:
        student = Student.objects.get(UserID = user.UserID)
        # print(student.RegNo)
        research = Research.objects.get(StuID = student.StuID)
        # print(research.ResID)

        recommendation = Recommendation.objects.filter(ResID = research.ResID)
        serializer = RecommendationsSerializer(recommendation, many=True)
        return Response(serializer.data, status=200)
    except:
        return Response("No comment found on your research")


# grade the Research
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def sendGrade(request):
    user = request.user
    if user.is_staff:
        serializer = ResultSerializer(data=request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    return Response('You have not access to this operation')

@api_view(['GET'])
def getAllResult(request):
    result = Result.objects.all()
    serializer = ResearchSerializer(result, many=True)
    return Response(serializer.data, status=200)

# Allocation

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def AllocateStudent(request):
    user = request.user
    if user.is_PGO:
        serializer = AllocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 200)
        return Response(serializer.errors, status=400)
    else:
        return Response("Access Denied")
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAllocation(request):
    user = request.user
    if user.is_supervisor:
        try:
            supervisor = Supervisor.objects.get(UserID = user.UserID)
            allocation = Allocation.objects.filter(SupID = supervisor.SupID)
            serializer = AllocationSerializer(allocation, many=True)
            return Response(serializer.data, status=200)
        except Supervisor.DoesNotExist:
            return Response('Supervisor Not registered in supervisor table')
        
    elif user.is_examiner:
        try:
            examiner = Examiner.objects.get(UserID = user.UserID)
            allocation = Allocation.objects.filter(ExID = examiner.ExID)
            serializer = AllocationSerializer(allocation, many=True)
            return Response(serializer.data, status=200)
        except Examiner.DoesNotExist:
            return Response('Examiner is not registered in the examiner table')
        
    elif user.is_PGO:
        allocation = Allocation.objects.all()
        serializer = AllocationSerializer(allocation, many=True)
        return Response(serializer.data, status=200)
    else:
        try:
            student = Student.objects.get(UserID = user.UserID)
            allocation = Allocation.objects.get(StuID = student.StuID)
            serializer = AllocationSerializer(allocation)
            return Response(serializer.data, status=200)
        except Student.DoesNotExist:
            return Response('Student is not registered in the student table')

# PGO
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def signPGO(request):
    user = request.user
    if user.is_superuser:
        serializer = PGOSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    return Response("Access Denied")

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getPGO(request):
    pgo = PostGraduateOfficer.objects.all()
    serializer = PGOSerializer(pgo, many=True)
    return Response(serializer.data, status=200)

# Examiner
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def signExaminer(request):
    user = request.user
    if user.is_superuser:
        serializer = ExaminerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    return Response("Access Denied")

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getExaminer(request):
    examiner = Examiner.objects.all()
    serializer = ExaminerSerializer(examiner, many=True)
    return Response(serializer.data, status=200)

@api_view(['DELETE'])
def deleteExaminer(request):
    examiner = Examiner.objects.all()
    examiner.delete()
    return Response("All examiner deleted")

# Supervisor
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def signSupervisor(request):
    user = request.user
    if user.is_superuser:
        serializer = SupervisorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    return Response("Access Denied")

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getSupervisor(request):
    supervisor = Supervisor.objects.all()
    serializer = SupervisorSerializer(supervisor, many=True)
    return Response(serializer.data, status=200)