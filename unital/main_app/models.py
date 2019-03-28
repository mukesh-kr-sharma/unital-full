from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _
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
    USER_TYPE = (('student','Student'),
        ('faculty','Faculty'),
        ('admin','Admin'), 
        ('guest','Guest'), 
        ('none','Not Known')
    )

class College(models.Model):
    clg_name = models.CharField(max_length=100)
    clg_u_name = models.CharField(max_length=100, unique=True)
    desc = models.TextField() # Description
    logo = models.ImageField(upload_to='college/%s/logo/' % clg_u_name, default='college/logo_default.png')
    clg_pic = models.ImageField(
        upload_to='college_list/home_pics/', default='college_list/home_pics/default.jpeg')

    def __str__(self):
        return self.clg_u_name

class User(AbstractUser, Choices):
    user_type = models.CharField(_('user type'), max_length=30, choices=Choices.USER_TYPE, default='none')
    college = models.ForeignKey(College, on_delete=models.CASCADE, related_name='user')
    department = models.CharField(max_length=50, choices=Choices.DEPARTMENT_CHOICES, default='CAPP')
    gender = models.CharField(max_length=1, choices=Choices.GENDER_CHOICES, null=True, default='O')
    phone_no = models.CharField(max_length=10, null=True, default='')
    address = models.TextField(null=True, default='')
    dob = models.DateField(_('date of birth'), null=True, default=timezone.now)
    profile_pic = models.ImageField(_('Profile Picture'), upload_to='%s/profile_pics/' % user_type)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'User'

# class Admin(models.Model, Choices):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     profile_pic = models.ImageField(upload_to='admin/profile_pics/')
#     user.is_admin = True
#     def __str__(self):
#         return self.user.username

# class Department(models.Model, Choices):
#     name = models.CharField(max_length=50, choices=Choices.DEPARTMENT_CHOICES, default='CAPP')

# class Faculty(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='faculty')
#     user.is_faculty = True
#     college = models.ForeignKey(College, on_delete=models.CASCADE, related_name='faculty')
#     profile_pic = models.ImageField(upload_to='faculty/profile_pics/')
#     dept = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="faculty")

#     def __str__(self):
#         return self.user.username

class Exam(models.Model):
    organisor = models.ForeignKey(User, 
                                on_delete=models.CASCADE, 
                                related_name='exam', 
                                limit_choices_to={'user_type': 'faculty'})
                                
    instructions = models.TextField()


# class Student(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='student')
#     college = models.ForeignKey(College, on_delete=models.CASCADE, related_name='student')
#     dept = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="student")
    
########### UNITAL NOTICE BOARD #############
class Notice(models.Model):
    def thirty_day_hence():
        """ Hii """
        return timezone.now() + timezone.timedelta(days=30)

    title = models.CharField(max_length=400)
    body = models.TextField()
    link = models.URLField()
    pub_date = models.DateField(default=timezone.now)
    expire_date = models.DateField(default=thirty_day_hence)

    def __str__(self):
        return str(self.id) + '. ' + self.pub_date.strftime("%d-%b-%Y")

######### COLLEGE PIC SLIDESHOW ################
def college_pic_path(instance, filename):
    return 'college/{0}/{1}'.format(str(instance.college.id) + '_' + instance.college.clg_u_name, filename)

class CollegePictures(models.Model):
    college = models.ForeignKey(College, on_delete=models.CASCADE, related_name='pictures')    
    pic = models.ImageField(upload_to=college_pic_path)
    def __str__(self):
        return str(self.id) + ' ' + self.college.clg_u_name


######### COLLEGE NOTICE BOARD #############
class CollegeNotice(Notice):
    college = models.ForeignKey(College, on_delete=models.CASCADE, related_name='notice')
    def __str__(self):
        return str(self.id) + '. ' + self.pub_date.strftime("%d-%b-%Y")
    
    
    
# about college, photu, principle message
