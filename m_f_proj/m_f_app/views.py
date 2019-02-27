from django.http import HttpResponse
from django.shortcuts import render


# This view handles the landing page
def index(request):
    return render(request, 'm_f_app/index.html')


# This page will provide a form to add users
def users(request):
    return render(request, 'm_f_app/users.html')
