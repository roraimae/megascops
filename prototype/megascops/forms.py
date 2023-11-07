from django import forms
from .models import User
class UserRegistrationForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    date_of_birth = forms.DateField()
    gender = forms.ChoiceField(choices=[('M', 'Masculino'), ('F', 'Feminino')])
    status = forms.CharField(max_length=100, widget=forms.HiddenInput(), initial='ACTIVE')
    role = forms.CharField(max_length=100, widget=forms.HiddenInput(), initial='USER')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'date_of_birth', 'gender', 'status', 'role']