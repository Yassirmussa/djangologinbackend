from rest_framework import serializers

from . models import Program, Student,Todos
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
        