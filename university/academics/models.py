from operator import truediv
from re import T
from django.db import models

from account.models import User
# # Create your models here.

class Supervisor(models.Model):
    SupID = models.AutoField(primary_key=True)
    UserID = models.OneToOneField(User, on_delete=models.CASCADE)
    class Meta:
        db_table = 'Supervisor'

class Examiner(models.Model):
    ExID = models.AutoField(primary_key=True)
    UserID = models.OneToOneField(User, on_delete=models.CASCADE)
    class Meta:
        db_table = 'Examiner'

class PostGraduateOfficer(models.Model):
    PgoID = models.AutoField(primary_key=True)
    UserID = models.OneToOneField(User, on_delete=models.CASCADE)
    class Meta:
        db_table = 'postGraduateOfficer'

program_choices = (
    ('BITAM', 'BACHELOR OF IT APPLICATION AND MANAGEMENT'),
    ('BCS', 'BACHELOR OF SCIENCE IN COMPUTER SCIENCE'),
    ('BAGES','BACHELOR OF ART IN GEORGRAPHY AND ENVIRONMENTAL STUDIES')
)

class Student(models.Model):
    StuID = models.AutoField(primary_key=True)
    Program = models.CharField(max_length=10, choices=program_choices)
    RegNo = models.CharField(max_length=250, unique=True)
    UserID = models.OneToOneField(User, on_delete=models.CASCADE)
    class Meta:
        db_table = 'student'


document_choice = (
    ('concept_note', 'ConceptNote'),
    ('proposal', 'Proposal'),
    ('progres_report', 'ProgresReport')
)

status_choices = (
    ('new', 'NEW'),
    ('progress','PROGRES'),
    ('completed', 'COMPLETED')
)
class Research(models.Model):
    ResID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=250)
    DocumentType = models.CharField(max_length=100, choices=document_choice)
    Document = models.FileField(upload_to='documents')
    Status = models.CharField(max_length=100, choices=status_choices, default='new')
    is_approved = models.BooleanField(default=False)
    StuID = models.OneToOneField(Student, on_delete=models.CASCADE)
    class Meta:
        db_table = 'research'

class Recommendation(models.Model):
    RecID = models.AutoField(primary_key=True)
    Description = models.CharField(max_length=250)
    ResID = models.ForeignKey(Research, on_delete=models.CASCADE)
    SupID = models.ForeignKey(Supervisor, blank=True ,on_delete=models.CASCADE)
    ExID = models.OneToOneField(Examiner, blank=True ,on_delete=models.CASCADE)
    class Meta:
        db_table = 'recommendation'

grade_choices = (
    ('A','A'),
    ('B+', 'B+'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
    ('E', 'E')
)

class Result(models.Model):
    RID = models.AutoField(primary_key=True)
    Grade = models.CharField(max_length=2, choices=grade_choices)
    ResID = models.OneToOneField(Research, on_delete=models.CASCADE)
    ExID = models.OneToOneField(Examiner, on_delete=models.CASCADE)
    class Meta:
        db_table = 'result'

class Allocation(models.Model):
    AID = models.AutoField(primary_key=True)
    StuID = models.OneToOneField(Student, on_delete=models.CASCADE)
    SupID = models.ForeignKey(Supervisor, on_delete=models.CASCADE)
    ExID = models.OneToOneField(Examiner, on_delete=models.CASCADE)
    class Meta:
        db_table = 'allocation'