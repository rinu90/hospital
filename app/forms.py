from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Patient, Doctor
from django.contrib.auth.forms import AuthenticationForm

# Patient Signup Form
class PatientSignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    address_line1 = forms.CharField(max_length=255)
    city = forms.CharField(max_length=100)
    state = forms.CharField(max_length=100)
    pincode = forms.CharField(max_length=6)
    profile_picture = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'address_line1', 'city', 'state', 'pincode','profile_picture']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()

        patient = Patient(user=user, address_line1=self.cleaned_data['address_line1'],
                          city=self.cleaned_data['city'], state=self.cleaned_data['state'],
                          pincode=self.cleaned_data['pincode'],profile_picture=self.cleaned_data['profile_picture'])
        patient.save()
        return user

# Doctor Signup Form
class DoctorSignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    address_line1 = forms.CharField(max_length=255)
    city = forms.CharField(max_length=100)
    state = forms.CharField(max_length=100)
    pincode = forms.CharField(max_length=6)
    specialization = forms.CharField(max_length=100)
    license_number = forms.CharField(max_length=100)
    profile_picture = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'address_line1', 'city', 'state', 'pincode', 'specialization', 'license_number','profile_picture']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()

        doctor = Doctor(user=user, address_line1=self.cleaned_data['address_line1'],
                        city=self.cleaned_data['city'], state=self.cleaned_data['state'],
                        pincode=self.cleaned_data['pincode'], specialization=self.cleaned_data['specialization'],
                        license_number=self.cleaned_data['license_number'],profile_picture=self.cleaned_data['profile_picture'])
        doctor.save()
        return user

# Create a SigninForm that extends Django's built-in AuthenticationForm
class SigninForm(AuthenticationForm):
    # You can customize the form fields, but by default, it already includes fields like 'username' and 'password'
    username = forms.CharField(max_length=150, required=True, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), required=True)

    class Meta:
        model = User
        fields = ['username', 'password']