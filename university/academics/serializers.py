from rest_framework import serializers

from . models import Program, Student, StudentCourse,Todos,Course
from account.serializers import UserSerializer


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = '__all__'

class TodosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todos
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    program = ProgramSerializer(source='ProID', read_only=True)
    user = UserSerializer(source = 'UserID', read_only=True)
    class Meta:
        model = Student
        fields = ['StuID', 'UserID','user','ProID','program']

class CourseSerializer(serializers.ModelSerializer):
    program = ProgramSerializer(source='ProID', read_only=True)
    class Meta:
        model = Course
        fields = ['CoID','CoTitle','CoCode','Coursework','Exam','ProID','program']

class StudentCourseSerializer(serializers.ModelSerializer):
    student = StudentSerializer(source="StuID", read_only=True)
    course = CourseSerializer(source="CoID", read_only=True)
    class Meta:
        model = StudentCourse
        fields = ['SCID','Coursework','Exam','StuID','student','CoID','course']