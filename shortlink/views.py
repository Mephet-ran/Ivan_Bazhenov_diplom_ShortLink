from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from shortlink.forms import ShortLinkForm
from .models import ShortLink
from django.contrib.auth.decorators import login_required


def HomePage(request):
    return render(request, 'shortlink/home.html', {'title': 'Главная страница'})


@login_required
def createLinkPage(request):
    if request.method == "POST":
        form = ShortLinkForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('short')
    else:
        form = ShortLinkForm()

    links = ShortLink.objects.filter(user=request.user)

    data = {
        'title': 'Создание сокращений',
        'form': form,
        'links': links
    }
    return render(request, 'shortlink/short.html', data)




