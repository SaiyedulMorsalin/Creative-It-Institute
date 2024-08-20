from django.shortcuts import render, redirect

from .forms import AddStudentForm
from django.contrib import messages
from .models import AddStudent


# Create your views here.


def student_list(request):
    all_student = AddStudent.objects.all()
    return render(request, "student_list.html", {"students": all_student})
