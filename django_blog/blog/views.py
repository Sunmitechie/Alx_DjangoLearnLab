from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm

def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("blog:home")
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/register.html", {"form": form})

@login_required
def profile_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
        else:
         form = CustomUserCreationForm(instance=request.user)
    return render(request, "registration/profile.html", {"form": form})
    