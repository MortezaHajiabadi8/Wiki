from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
        
    vote = models.IntegerField(default=0)   
    
 

    def __str__(self):
        return self.user.username

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
        
    
    
 

    def __str__(self):
        return self.user.username

class Thesis(models.Model):
    owner = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, default='hamidabdoli')
    file = models.FileField(upload_to='theses', blank=False)
    
    
    
    def __str__(self):
        return self.subject
    
    
