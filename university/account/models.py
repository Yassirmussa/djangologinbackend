from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

gender_choices = (
    ('M','Male'),
    ('F','Female')
)

class User(AbstractUser):
    UserID = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    
    phonenumber = models.CharField(max_length=10)
    address = models.CharField(max_length=250)
    gender = models.CharField(max_length=1, choices=gender_choices)

    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name="user_groups",
        related_query_name="users",
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name="user_permissions",
        related_query_name="users",
    )

    class Meta:
        db_table = 'users'
