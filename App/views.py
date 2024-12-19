from django.shortcuts import render, redirect

from . import models
from .forms import RentalAdForm
from django.contrib.auth import login, authenticate

from .forms import RegistrationForm
from .forms import AdForm
from .models import Ad


def home(request):
    context = {
        'title': 'Домашняя страница',
        'heading': 'Добро пожаловать на сайт!',
        'content': 'Это контент домашней страницы',
    }
    return render(request, 'home.html', context)


def about(request):
    context = {
        'title': 'О нас',
        'heading': 'Кто мы?',
        'content': 'Здесь можно рассказать о компании или проекте.',
    }
    return render(request, 'about.html', context)


def contact(request):
    context = {
        'title': 'Контактная информация',
        'heading': 'Свяжитесь с нами',
        'content': 'Укажите контактные данные здесь.',
    }
    return render(request, 'contact.html', context)


def create_ad(request):
    if request.method == 'POST':
        form = RentalAdForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'App/success.html')
    else:
        form = RentalAdForm()
    return render(request, 'create.html', {'form': form})


def ad_success(request):
    return render(request, 'success.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'registration/login.html', {'error_message': 'Invalid login'})
    else:
        return render(request, 'registration/login.html')


def create_ad(request):
    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.save()
            return redirect('home')
    else:
        form = AdForm()
    return render(request, 'create_ad.html', {'form': form})


def approve_ad(request):
    ads = Ad.objects.filter(is_approved=False)
    if request.method == 'POST':
        for ad in ads:
            if str(ad.id) in request.POST:
                ad.is_approved = True
                ad.save()
        return redirect('home')
    return render(request, 'approve_ad.html', {'ads': ads})


def add_ad_to_database(ad_data):
    try:
        ad = Ad.objects.create(
            title=ad_data['title'],
            image=ad_data['image'],
            description=ad_data['description'],
            is_approved=ad_data['is_approved']
        )
        return f"Объявление '{ad.title}' успешно добавлено"
    except Exception as e:
        return f'Не удалось добавить объявление: {e}'