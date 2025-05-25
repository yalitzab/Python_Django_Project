from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def register(request):
    # This function renders the registration page for users
    form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})