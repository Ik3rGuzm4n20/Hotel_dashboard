from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# --- LOGIN ---
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # redirige al dashboard
        else:
            return render(request, 'core/login.html', {'form': {'errors': True}})
    return render(request, 'core/login.html')

# --- LOGOUT ---
def logout_view(request):
    logout(request)
    return redirect('login')

# --- DASHBOARD ---
@login_required(login_url='login')
def dashboard(request):
    return render(request, 'core/dashboard.html')