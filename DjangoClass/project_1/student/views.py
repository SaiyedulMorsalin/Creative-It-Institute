from django.shortcuts import render, redirect

from .forms import AddStudentForm


# Create your views here.
def add_student(request):
    if request.method == "POST":
        form = AddStudentForm(request.POST, request.FILES)
        if form.is_valid():

            form.save()
            return redirect("student_list")

    form = AddStudentForm()
    return render(request, "add_student.html", {"form": form})


def student_list(request):

    return render(request, "student_list.html")
