from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.shortcuts import render, redirect

from .forms import *
# Create your views here.
def home_page(request):
    tovar=tovars.objects.all()
    return render (request,'home.html',{'tovar':tovar})


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')  # После успешной регистрации перенаправляем на страницу входа
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def profile(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfileEditForm(instance=request.user)
    return render(request, 'profile.html', {'form': form})

from django.shortcuts import render, redirect
from .forms import MessageForm

def send_message(request, user_id):
    user = CustomUser.objects.get(id=user_id)

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']

            Review.objects.create(name=user.username, content=message, sender=sender)

            return redirect('profile')
    else:
        form = MessageForm()

    return render(request, 'send_message.html', {'form': form, 'receiver': user})

# Ваши импорты

def search_user(request):
    if request.method == 'GET':
        query = request.GET.get('q')  # Получаем запрос из GET-параметра 'q'
        if query:
            users = CustomUser.objects.filter(username__icontains=query)
        else:
            users = CustomUser.objects.all()
    else:
        users = CustomUser.objects.all()

    return render(request, 'search_user.html', {'users': users})
from django.shortcuts import render

