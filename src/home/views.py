from django.shortcuts import render

# Create your views here.


# the home page
def index(request):
    return render(request, '../templates/index.html')