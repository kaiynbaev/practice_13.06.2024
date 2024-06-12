from django.contrib import admin
from .models import UserModel

class UserModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', )

admin.site.register(UserModel, UserModelAdmin)