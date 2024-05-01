from django import forms
from .models import Students

class StudentForm(forms.ModelForm):
    class Meta:
        model=Students
        fields=['register_number','full_name','email','department','mobile_number']
        labels={
            'register_number': 'Registration Number',
            'full_name': 'Name',
            'email': 'Email',
            'department': 'Department',
            'mobile_number':'Mobile Number'
        }
        widgets={
            'register_number': forms.NumberInput(attrs={'class':'form-control'}),
            'full_name': forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'department':forms.Select(attrs={'class':'form-control'}),
            'mobile_number':forms.TextInput(attrs={'class':'form-control'})
        }