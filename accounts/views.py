from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request, 'accounts/register.html')

def login(request):
    return render(request, 'accounts/login.html')