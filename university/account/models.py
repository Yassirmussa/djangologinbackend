from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    UserID = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    username = None
    
    
    PhoneNumber = models.CharField(max_length=10)
    Address = models.CharField(max_length=250)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name="user_groups",
        related_query_name="user",
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name="user_permissions",
        related_query_name="user",
    )

    class Meta:
        db_table = 'users'
