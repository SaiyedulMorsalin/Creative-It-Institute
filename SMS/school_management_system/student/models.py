from django.db import models
from django.contrib.auth.models import User
from .constants import GENDER_TYPE,STUDENT_TYPE
from department.models import Department
from address.models import PermanentAddress,PresentAddress
from course.models import Course
# Create your models here.

class StudentProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='student_user')
    bio = models.TextField()
    mobile_number = models.CharField(max_length=11)
    gender = models.CharField(max_length=10,choices=GENDER_TYPE)
    student_type = models.CharField(max_length=15,choices=STUDENT_TYPE)
    department = models.OneToOneField(Department,on_delete=models.CASCADE,related_name="student_department")
    registration_id = models.PositiveIntegerField()
    secret_key = models.CharField(max_length=6,null=True,blank=True)
    permanent_address = models.OneToOneField(PermanentAddress,on_delete=models.CASCADE,related_name="student_permanent_address")
    present_address = models.OneToOneField(PresentAddress,on_delete=models.CASCADE,related_name="student_present_address")
    otp = models.CharField(max_length=6,null=True,blank=True)
    courses = models.ForeignKey(Course,on_delete=models.CASCADE,related_name="student_courses")