from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated

from academics.models import Examiner, PostGraduateOfficer, Student,Research,Recommendation,Result, Supervisor
from academics.serializers import ExaminerSerializer, PGOSerializer, StudentSerializer, ResearchSerializer, RecommendationsSerializer, ResultSerializer, SupervisorSerializer

# Handle Staff registration by Admin
# insert 
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def registerSupervisor(request):
    user = request.user
    if user.is_superuser:
        serializer = SupervisorSerializer(data=request.data)
        if serializer.is_valid:
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
        if serializer.is_valid:
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
        if serializer.is_valid:
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
    if not user.is_superuser and not user.is_staff:
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid:
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
    if not user.is_superuser and not user.is_staff:
        serializer = ResearchSerializer(data=request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    return Response('You have not access to this operation')

@api_view(['GET'])
def getAllResearch(request):
    research = Research.objects.all()
    serializer = ResearchSerializer(research, many=True)
    return Response(serializer.data, status=200)


# send Recommendation
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def sendRecommendation(request):
    user = request.user
    if user.is_staff:
        serializer = RecommendationsSerializer(data=request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    return Response('You have not access to this operation')

@api_view(['GET'])
def getAllRecommendation(request):
    recommendation = Recommendation.objects.all()
    serializer = RecommendationsSerializer(recommendation, many=True)
    return Response(serializer.data, status=200)


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