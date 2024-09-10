from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from student.models import StudentProfile


# Create your views here.
@login_required(login_url="student_login")
def home_page(request):
    return render(request, "index.html")


@login_required(login_url="student_login")
def student_profile(request):
    student = request.user
    student_profile = StudentProfile.objects.filter(user=student)
    print(student.first_name)
    return render(request, "student_profile.html")
