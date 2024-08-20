from django.db import models


# Create your models here.
class AddStudent(models.Model):
    roll = models.PositiveIntegerField()
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=50)
    student_img = models.ImageField(upload_to="media")
