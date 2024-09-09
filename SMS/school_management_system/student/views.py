from django.shortcuts import render


# Create your views here.
def student_register(request):
    if request.method == "POST":
        pass
    return render(request, "student_register.html")
