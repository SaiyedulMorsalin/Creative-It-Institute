from django.shortcuts import render, redirect

from student.forms import AddStudentForm
from django.contrib import messages
from student.models import AddStudent


def home_page(request):
    if request.method == "POST":
        form = AddStudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Successfully added this student information....."
            )
            return redirect("student_list")
        else:
            messages.error(request, "Please Write valid student information.....")
    all_student = AddStudent.objects.all()
    form = AddStudentForm()
    return render(request, "index.html", {"form": form, "students": all_student})
