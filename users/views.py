from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.


def register(request):
    if request.method == 'POST':  # if form is submitted
        form = UserCreationForm(request.POST)
        # hold submitted data in 'form'

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')  # cleaned_data is data after validation
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else:
        # else show a new empty form
        form = UserCreationForm()

    return render(request, 'users/register.html', {'form': form})
