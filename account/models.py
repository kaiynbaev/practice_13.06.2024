from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserModelManager
# from posts.models import Posts
 
class UserModel(AbstractUser):
    email = models.EmailField(db_index=True, max_length=200, null=True)
    name = models.CharField(max_length=200, unique=True)
    contact_information = models.CharField(max_length=50, null=False)
    city_address = models.CharField(max_length=200, null=False)
    # posts = models.ForeignKey(Posts, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    is_contractor = models.BooleanField(default=False) # Показывает, является ли пользователь подрядчиком
    objects = UserModelManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'email', 'contact_information', 'city_address', 'is_contractor']
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username