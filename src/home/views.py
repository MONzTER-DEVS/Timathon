from django.shortcuts import render

# Create your views here.


# the home page
def index(request):
    return render(request, '../templates/home/index.html')


def components(request):
    return render(request, '../templates/components/components.html')


def favourites(request):
    return render(request, '../templates/home/favourites.html')


