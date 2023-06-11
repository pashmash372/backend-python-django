from django.http import HttpResponse
from django.shortcuts import render
from .models import User


def index(request):
    # len(User.objects.all()) dont use this bad practice
    count_of_users = User.objects.count()
    users= User.objects.all()

    for user in users:
        print(user.name)

    context = {
        'count_of_users': count_of_users,
        'users':users
    }
    return render(request, 'users/index.html', context=context)


def signup(request):
    
    return render(request, 'users/signup.html')