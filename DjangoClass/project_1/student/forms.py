from django import forms
from .models import AddStudent


class AddStudentForm(forms.ModelForm):
    class Meta:
        model = AddStudent
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field == "student_img":
                self.fields[field].widget.attrs.update(
                    {
                        "class": "file-input file-input-bordered file-input-primary w-full max-w-xs",
                        "type": "file",
                    }
                )
            else:
                self.fields[field].widget.attrs.update(
                    {
                        "class": "input input-bordered input-primary w-full max-w-xs",
                        "type": "text",
                    }
                )
