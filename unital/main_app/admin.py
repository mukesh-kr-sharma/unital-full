from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'user_type', 'department', 'email')
    list_filter = ('user_type', 'college', 'department')
    
    fields = ('first_name', 
              'last_name', 
              'username', 
              'password', 
              'email',
              'profile_pic', 
              'user_type', 
              'college',
              'department',
              'gender', 
              'phone_no', 
              'dob', 
              'address' )
    # exclude = ('user_permissions','groups','is_staff', 'is_active','last_login','date_joined',) 
    list_display_links = ('id', 'username')
    search_fields = ('username', 'first_name')
    list_per_page = 25

    def save_model(self, request, obj, form, change):
        password = str(obj.password)
        obj.set_password(password)
        super().save_model(request, obj, form, change)

class ExamAdmin(admin.ModelAdmin):
    pass
    # def __init__(self, *args, **kwargs):
    #     super(ExamAdmin, self).__init__(*args, **kwargs)
    #     self.fields['organisor'].queryset = User.objects.filter(user_type='faculty')


admin.site.register(User, UserAdmin)
admin.site.register(Notice)
admin.site.register(College)
admin.site.register(CollegePictures)
admin.site.register(CollegeNotice)
admin.site.register(Exam, ExamAdmin)
