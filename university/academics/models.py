from django.db import models

from account.models import User
# Create your models here.

class Program(models.Model):
    ProID  = models.AutoField(primary_key=True)
    ProName = models.CharField(max_length=250)
    ProDescription = models.CharField(max_length=250)
    ProCapacity = models.IntegerField()
    class Meta:
        db_table = 'program'


class Student(models.Model):
    StuID = models.AutoField(primary_key=True)
    
    UserID = models.OneToOneField(User, on_delete=models.CASCADE)

    ProID = models.OneToOneField(Program, on_delete=models.CASCADE)

    class Meta:
        db_table = 'student'


class Course(models.Model):
    CoID = models.AutoField(primary_key=True)
    CoTitle = models.CharField(max_length=250)
    CoCode = models.CharField(max_length=250)
    Coursework = models.IntegerField()
    Exam = models.IntegerField()
    ProID = models.ForeignKey(Program, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'course'


class StudentCourse(models.Model):
    SCID = models.AutoField(primary_key=True)
    Coursework = models.IntegerField()
    Exam = models.IntegerField()
    StuID = models.ForeignKey(Student, on_delete=models.CASCADE)
    CoID = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        db_table = 'studentcourse'


class Todos(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    completed = models.BooleanField(default = False)
    class Meta:
        db_table = 'todos'



