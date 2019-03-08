from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Admin(models.Model):
    def imgUploadPath(self):
        return 'profile_pics/'+str(self.user.id)

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    access_to = models.CharField(max_length=150)
    profile_pic = models.ImageField(upload_to='admin/profile_pics/')

    def __str__(self):
        return self.user.username

    
class Notice(models.Model):
    def thirty_day_hence():
        return timezone.now() + timezone.timedelta(days=30)

    title = models.CharField(max_length=400)
    body = models.TextField()
    link = models.URLField()
    pub_date = models.DateField(default=timezone.now)
    expire_date = models.DateField(default=thirty_day_hence)

    def __str__(self):
        return str(self.id) + '. ' + self.pub_date.strftime("%d-%b-%Y")
    
class CollegeList(models.Model):
    clg_name = models.CharField(max_length=100)
    clg_u_name = models.CharField(max_length=100, unique=True)
    desc = models.TextField()
    clg_pic = models.ImageField(upload_to='college_list/home_pics/', default='college_list/home_pics/default.jpeg')

    def __str__(self):
        return self.clg_u_name
