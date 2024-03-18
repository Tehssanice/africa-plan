from django.shortcuts import render

# Create your views here.


def index(request):
    name = 'Tessa'

    content = {'name': name}

    return render(request, 'index.html', content)
