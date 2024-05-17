from django.shortcuts import render, redirect
from .models import Photo, Category
from .forms import PhotoForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError


def home(request):
    photos = Photo.objects.filter(user=request.user)
    return render(request, 'photos/home.html', {'photos': photos})


def photo_list(request):
    ...


def photo_add(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()
            return redirect('photo_list')
    else:
        form = PhotoForm()
    return render(request, 'photos/photo_add.html', {'form': form})


def loginuser(request):
    if request.method == "GET":
        return render(request, 'photos/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'photos/loginuser.html', {'form': AuthenticationForm(),
                                                             'error': 'Не верные данные для входа'})
        else:
            login(request, user)
            return redirect('home')


def registr(request):
    if request.method == "GET":
        return render(request, 'photos/registr.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect("home")
            except IntegrityError:
                return render(request, 'photos/registr.html.html',
                              {'form': UserCreationForm()},
                              {'error': "Такое имя существует. Задайте другое имя"})

        else:
            print("Пароли не совпали")
            return render(request, 'photos/registr.html.html',
                          {'form': UserCreationForm()},
                          {'error': "Пароли не совпали"})


def currenttodos(request):
    return render(request, 'photos/loginuser.html')
