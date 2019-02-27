from django.http import HttpResponse
from django.shortcuts import render

# This view handles the landing page
from .forms import NewUserForm


def index(request):
    return render(request, 'm_f_app/index.html')


# This page will provide a form to add users
def users(request):
    user_form = NewUserForm()

    if request.method == "POST":
        print('Got posted data')

    return render(request, 'm_f_app/users.html', {'userform': user_form})
