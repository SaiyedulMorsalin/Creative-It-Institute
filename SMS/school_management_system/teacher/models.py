from django.db import models
from .constants import GENDER_TYPE
from django.contrib.auth.models import User
# Create your models here.
from address.models import PermanentAddress,PresentAddress
from department.models import Department
class TeacherProfile(models.Model):
    user = models.OneToOneField(User)
    bio = models.TextField()
    mobile_number = models.CharField(max_length=11)
    gender = models.CharField(max_length=10,choices=GENDER_TYPE)
    department =models.ForeignKey(Department,on_delete=models.CASCADE,related_name="teacher_departments")
    date_of_birth = models.DateField()
    present_address = models.OneToOneField(PresentAddress,on_delete=models.CASCADE,related_name="teacher_present_address")
    permanent_address = models.OneToOneField(PermanentAddress,on_delete=models.CASCADE,related_name="teacher_permanent_address")
    secret_key = models.CharField(max_length=6,null=True,blank=True)
    otp = models.CharField(max_length=6,null=True,blank=True)
    