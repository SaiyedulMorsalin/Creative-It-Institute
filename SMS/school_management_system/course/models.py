from django.db import models
from department.models import Department
from teacher.models import TeacherProfile
# Create your models here.
class Course(models.Model):
    course_title = models.TextField()
    department = models.ForeignKey(Department,on_delete=models.CASCADE,related_name="course_department")
    course_duration = models.TextField()
    available_seat = models.PositiveIntegerField()
    teacher = models.OneToOneField(TeacherProfile,related_name="course_teacher",on_delete=models.CASCADE)
    course_details = models.TextField()
    course_available = models.BooleanField(default=True)
    