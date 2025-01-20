from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import PatientSignupForm, DoctorSignupForm, SigninForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Patient, Doctor
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


# View for handling patient signup
def patient_signup_view(request):
    if request.method == 'POST':
        form = PatientSignupForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user
            login(request, user)  # Log the user in
            return redirect('patient_dashboard')  # Redirect to patient dashboard
    else:
        form = PatientSignupForm()
    return render(request, 'signup.html', {'form': form, 'user_type': 'patient'})

# View for handling doctor signup
def doctor_signup_view(request):
    if request.method == 'POST':
        form = DoctorSignupForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user
            login(request, user)  # Log the user in
            return redirect('doctor_dashboard')  # Redirect to doctor dashboard
    else:
        form = DoctorSignupForm()
    return render(request, 'signup.html', {'form': form, 'user_type': 'doctor'})

# View for handling login (both for patient and doctor)
def signin_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                if hasattr(user, 'patient'):
                    return redirect('patient_dashboard')
                elif hasattr(user, 'doctor'):
                    return redirect('doctor_dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'signin.html', {'form': form})

# Dashboard for patient
@login_required
def patient_dashboard_view(request):
    return render(request, 'patient_dashboard.html')

# Dashboard for doctor
@login_required
def doctor_dashboard_view(request):
    return render(request, 'doctor_dashboard.html')

def logout_view(request):
    # Logs out the user and redirects to the login page
    logout(request)
    return redirect('signin')


# Registration View (for both Patient and Doctor)
def register(request):
    patient_form = PatientSignupForm()
    doctor_form = DoctorSignupForm()
    signin_form = SigninForm()
    if request.method == 'POST':
        # Check if it's a registration or login action
        if 'patient_signup' in request.POST:
            patient_form = PatientSignupForm(request.POST)
            if patient_form.is_valid():
                patient_form.save()
                return redirect('signin')  # Redirect to login after successful registration
        elif 'doctor_signup' in request.POST:
            doctor_form = DoctorSignupForm(request.POST)
            if doctor_form.is_valid():
                doctor_form.save()
                return redirect('signin')  # Redirect to login after successful registration
        elif 'signin' in request.POST:
            signin_form = SigninForm(request.POST)
            print("Sign in form POST data:", request.POST)
            if signin_form.is_valid():
                username = signin_form.cleaned_data['username']
                password = signin_form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('doctor_dashboard')  # Redirect to dashboard after successful login
                else:
                    signin_form.add_error(None, 'Invalid username or password')
    else:
        # If the form is not submitted, show empty forms
        signin_form = None

    return render(request, 'register.html', {
        'patient_form': patient_form,
        'doctor_form': doctor_form,
        'signin_form': signin_form
    })

