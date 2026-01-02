from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            password=password1
        )

        login(request, user)
        return redirect('issue_list')

    return render(request, 'accounts/register.html')
