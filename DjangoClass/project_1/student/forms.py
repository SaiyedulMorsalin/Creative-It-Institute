from django import forms
from .models import AddStudent


class AddStudentForm(forms.ModelForm):
    class Meta:
        model = AddStudent
        fields = "__all__"
