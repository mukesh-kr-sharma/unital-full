from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.

# admin.site.register(User, UserAdmin)
admin.site.register(User)
admin.site.register(Admin)
admin.site.register(Faculty)
admin.site.register(Notice)
admin.site.register(College)
admin.site.register(CollegePictures)
admin.site.register(CollegeNotice)
