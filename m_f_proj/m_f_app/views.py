from django.http import HttpResponse
from django.shortcuts import render

# This view handles the landing page
from .forms import NewUserForm


def index(request):
    return render(request, 'm_f_app/index.html')


# This page will provide a form to add users
def users(request):
    new_form = NewUserForm()

    if request.method == "POST":
        print('Got posted data')
        new_form = NewUserForm(request.POST)
        if new_form.is_valid():
            new_form.save(commit=True)
            return index(request) # Go back to home
        else:
            print('Error Not Valid')

    return render(request, 'm_f_app/users.html', {'userform': new_form})
