from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .forms import CustomUserCreationForm, CustomAuthenticationForm

def home(request):
    return render(request, 'auth_app/home.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # Send welcome email
            subject = 'Welcome to Kingdoms Authentication App'
            html_message = render_to_string('auth_app/welcome_email.html', {'user': user})
            plain_message = strip_tags(html_message)
            from_email = 'noreply@kingdoms.com'
            to_email = user.email
            
            send_mail(subject, plain_message, from_email, [to_email], html_message=html_message)
            
            messages.success(request, 'Registration successful! Please check your email for a welcome message.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'auth_app/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
        else:
            # Add specific error message for invalid credentials
            messages.error(request, 'Invalid username or password. Please try again.')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'auth_app/login.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.info(request, 'You have been logged out successfully.')
    return redirect('home')

@login_required
def dashboard(request):
    return render(request, 'auth_app/dashboard.html')

class CustomPasswordResetView(PasswordResetView):
    template_name = 'auth_app/reset_password.html'
    email_template_name = 'auth_app/password_reset_email.html'
    success_url = '/reset-password-sent/'

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'auth_app/reset_sent.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'auth_app/reset_form.html'
    success_url = '/reset-password-complete/'

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'auth_app/reset_complete.html'
