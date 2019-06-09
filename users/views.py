from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':  # if form is submitted
        form = UserRegistrationForm(request.POST)
        # hold submitted data in 'form'

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')  # cleaned_data is data after validation
            messages.success(request, f'Account created for {username}! You may Log In now.')
            return redirect('login')
    else:
        # else show a new empty form
        form = UserRegistrationForm()

    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):

    # create instance of update forms
    u_form = UserUpdateForm(instance=request.user.profile)
    p_form = ProfileUpdateForm(instance=request.user.profile)

    # pass them to template
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)
