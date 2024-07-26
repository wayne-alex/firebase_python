from django.shortcuts import render

from .forms import SignUpForm


# Create your views here.
def login(request):
    return render(request, 'Login.html')


def register(request):
    form = SignUpForm()
    return render(request, 'register.html', {'form': form})


def dashboard(request):
    return render(request, 'dashboard.html')


def project(request):
    return render(request, 'project.html')
