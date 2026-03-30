from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'enrollment_no', 'division']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'enrollment_no': forms.TextInput(attrs={'class': 'form-control'}),
            'division': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_enrollment_no(self):
        enrollment_no = self.cleaned_data.get('enrollment_no')
        if not enrollment_no.isalnum():
            raise forms.ValidationError("Enrollment number must be alphanumeric.")
        return enrollment_no
