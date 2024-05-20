from rest_framework import serializers

from academics.models import Allocation, Examiner, PostGraduateOfficer, Student, Research, Recommendation, Result, Supervisor
from account.serializers import UserSerializer

class SupervisorSerializer(serializers.ModelSerializer):
    user = UserSerializer(source='UserID', read_only=True)
    class Meta:
        model = Supervisor
        fields = '__all__'
class ExaminerSerializer(serializers.ModelSerializer):
    user = UserSerializer(source='UserID', read_only=True)
    class Meta:
        model = Examiner
        fields = '__all__'

class PGOSerializer(serializers.ModelSerializer):
    user = UserSerializer(source='UserID', read_only=True)
    class Meta:
        model = PostGraduateOfficer
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer(source='UserID', read_only=True)
    supervisor = SupervisorSerializer(source='SupID', read_only=True)
    examiner = ExaminerSerializer(source='ExID', read_only=True)
    class Meta:
        model = Student
        fields = '__all__'

class ResearchSerializer(serializers.ModelSerializer):
    student = StudentSerializer(source='StuID', read_only=True)
    class Meta:
        model = Research
        fields = '__all__'

class RecommendationsSerializer(serializers.ModelSerializer):
    reseach = ResearchSerializer(source='ResID', read_only=True)
    supervisor = SupervisorSerializer(source='SupID', read_only=True)
    examiner = ExaminerSerializer(source='ExID', read_only=True)
    class Meta:
        model = Recommendation
        fields = '__all__'

class ResultSerializer(serializers.ModelSerializer):
    reseach = ResearchSerializer(source='ResID', read_only=True)
    class Meta:
        model = Result
        fields = '__all__'

class AllocationSerializer(serializers.ModelSerializer):
    student = StudentSerializer(source='StuID', read_only=True)
    supervisor = SupervisorSerializer(source='SupID', read_only=True)
    examiner = ExaminerSerializer(source='ExID', read_only=True)
    class Meta:
        model = Allocation
        fields = '__all__'