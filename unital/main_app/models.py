from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
# python manage.py migrate --run-syncdb
class Choices():
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others')
    )
    DEPARTMENT_CHOICES = (
        ('CAPP', 'Computer Application'),
        ('IT', 'Information Technology')
    )
    PROGRAMME_CHOICES = (
        ('UG', 'Undergraduate'),
        ('PG', 'Postgraduate')
    )

class User(AbstractUser):
    USER_TYPE = (('student','Student'), ('faculty','Faculty'), ('admin','Admin'), ('guest','Guest'), ('none','Not Known'))
    user_type = models.CharField(max_length=30, choices=USER_TYPE, default='none')
    gender = models.CharField(max_length=1, choices=Choices.GENDER_CHOICES, null=True, default='O')
    phone_no = models.CharField(max_length=10, null=True, default='00000')
    address = models.TextField(null=True, default='Fill it')
    dob = models.DateField(null=True, default=timezone.now)

class Admin(models.Model, Choices):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='admin/profile_pics/')
    user.is_admin = True
    def __str__(self):
        return self.user.username


class College(models.Model):
    clg_name = models.CharField(max_length=100)
    clg_u_name = models.CharField(max_length=100, unique=True)
    desc = models.TextField()
    clg_pic = models.ImageField(
        upload_to='college_list/home_pics/', default='college_list/home_pics/default.jpeg')

    def __str__(self):
        return self.clg_u_name

class Department(models.Model, Choices):
    name = models.CharField(max_length=50, choices=Choices.DEPARTMENT_CHOICES, default='CAPP')

class Faculty(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='faculty')
    user.is_faculty = True
    college = models.ForeignKey(College, on_delete=models.CASCADE, related_name='faculty')
    profile_pic = models.ImageField(upload_to='faculty/profile_pics/')
    dept = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="faculty")

    def __str__(self):
        return self.user.username

class Exam(models.Model):
    organisor = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='exam')
    instructions = models.TextField()


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='student')
    user.is_student = True
    dept = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="student")
    
class Notice(models.Model):
    def thirty_day_hence():
        """Hii"""
        return timezone.now() + timezone.timedelta(days=30)

    title = models.CharField(max_length=400)
    body = models.TextField()
    link = models.URLField()
    pub_date = models.DateField(default=timezone.now)
    expire_date = models.DateField(default=thirty_day_hence)

    def __str__(self):
        return str(self.id) + '. ' + self.pub_date.strftime("%d-%b-%Y")
    


