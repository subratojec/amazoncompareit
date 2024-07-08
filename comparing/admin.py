from django.contrib import admin
from comparing.models import Contact
from django.contrib.auth.admin import UserAdmin
from comparing.models import CustomUser


# Register your models here.
admin.site.register(Contact)
admin.site.register(CustomUser, UserAdmin)
