from django.shortcuts import render


# Create your views here.
def index(request):
    context = {}
    return render(request, 'my_app/index.html', context)


def search(request):
    context = {}
    return render(request, 'my_app/search.html', context)


def auth(request):
    context = {}
    return render(request, 'my_app/authentication.html', context)
