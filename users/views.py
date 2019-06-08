from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def register(request):
    if request.method == 'POST':  # if form is submitted
        form = UserCreationForm(request.POST)
        # hold submitted data in 'form'
    else:
        # else show a new empty form
        form = UserCreationForm

    return render(request, 'users/register.html', {'form': form})
