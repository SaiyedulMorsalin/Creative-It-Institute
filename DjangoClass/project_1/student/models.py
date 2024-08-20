from django.db import models


# Create your models here.
class AddStudent(models.Model):
    roll = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=100, unique=True)
    student_bio = models.TextField(max_length=500)
    department = models.CharField(max_length=50)
    student_img = models.ImageField(upload_to="media")
