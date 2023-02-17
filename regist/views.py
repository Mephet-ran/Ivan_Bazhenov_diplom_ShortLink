from django.shortcuts import render, redirect
from .forms import RegistForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

def register(request):
    if request.method == "POST":
        print(request.POST)
        form = RegistForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Пользователь  был успешно создан!')
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return redirect('/')
    else:
        form = RegistForm()

    return render(
        request,
        'regist/regist.html',
        {
            'form': form,
            'title': 'Регистрация'
        }

    )

@login_required()
def profile(request):
    if request.method == "POST":

        update = UserUpdateForm(request.POST, instance=request.user)

        if update.is_valid():
            update.save()

            messages.success(request, f'Пользователь был успешно обвновлён!')
            return redirect('profile')
    else:

        update = UserUpdateForm(instance=request.user)

    data = {
        'title': 'Профиль',
        'update': update
    }

    return render(request, 'regist/profile.html', data)