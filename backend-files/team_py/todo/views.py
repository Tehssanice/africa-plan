from django.shortcuts import render

# Create your views here.


def index(request):

    FirstName = "Jonah"
    LastName = "Onah"

    context = {"first_name": FirstName,  "last_name": LastName}
    return render(request, './todo/index.html', context)


def register(request):
    return render(request, './todo/register.html')


def login(request):
    return render(request, './todo/login.html')
