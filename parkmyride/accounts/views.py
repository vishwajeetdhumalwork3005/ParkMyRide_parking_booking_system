from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required

# Signup view
@require_http_methods(['GET', 'POST'])
def signup_view(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        password = request.POST.get('password')
        confirm = request.POST.get('confirm_password')
        if not all([full_name, email, password, confirm]):
            messages.error(request, 'Please fill all required fields')
            return redirect('signup')
        if password != confirm:
            messages.error(request, 'Passwords do not match')
            return redirect('signup')
        if User.objects.filter(username=email).exists():
            messages.error(request, 'User already exists')
            return redirect('signup')
        # Save full name and phone: simplified storage using first_name/last_name
        names = full_name.split(None, 1)
        first_name = names[0]
        last_name = names[1] if len(names) > 1 else ''
        user = User.objects.create_user(username=email, email=email, password=password,
                                        first_name=first_name, last_name=phone)
        login(request, user)
        return redirect('dashboard')
    return render(request, 'accounts/signup.html')

# Login view
@require_http_methods(['GET', 'POST'])
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        messages.error(request, 'Invalid credentials')
        return redirect('login')
    return render(request, 'accounts/login.html')

# Logout
def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
@require_http_methods(['GET', 'POST'])
def edit_profile(request):
    """Allow users to edit their profile: full name, email, phone.

    Note: phone is stored in `last_name` field for simplicity in this demo.
    """
    user = request.user
    if request.method == 'POST':
        full_name = request.POST.get('full_name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        if not full_name or not email:
            messages.error(request, 'Full name and email are required')
            return redirect('edit-profile')
        # store first token as first_name, phone into last_name (simple demo storage)
        user.first_name = full_name.split(None, 1)[0]
        user.email = email
        user.username = email
        user.last_name = phone
        user.save()
        messages.success(request, 'Profile updated')
        return redirect('dashboard')

    # Prefill form values
    context = {
        'full_name': user.first_name,
        'email': user.email,
        'phone': user.last_name,
    }
    return render(request, 'accounts/edit_profile.html', context)


@require_http_methods(['GET', 'POST'])
def password_reset(request):
    """Simple password reset: user submits email and new password.

    This is a demo-only flow (no email tokens). For production, use Django's
    password reset flow with email tokens.
    """
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        pwd = request.POST.get('password')
        conf = request.POST.get('confirm_password')
        if not email or not pwd or not conf:
            return render(request, 'accounts/password_reset.html', {'error': 'All fields required'})
        if pwd != conf:
            return render(request, 'accounts/password_reset.html', {'error': 'Passwords do not match'})
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return render(request, 'accounts/password_reset.html', {'error': 'No user with that email'})
        user.set_password(pwd)
        user.save()
        return render(request, 'accounts/password_reset.html', {'success': True})
    return render(request, 'accounts/password_reset.html')
