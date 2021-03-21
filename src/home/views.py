from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
# Create your views here.


# the home page
def index(request):
    return render(request, '../templates/home/index.html')


def components(request):
    return render(request, '../templates/components/components.html')


def favourites(request):
    return render(request, '../templates/home/favourites.html')


def charts(request):
    return render(request, '../templates/components/charts/charts.html')


def tables(request):
    parameters = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['datafile']
        if uploaded_file.name.endswith('.csv'):
            parameters = {'result': 'Correct File Uploaded'}
        else:
            parameters = {'result': 'Incorrect File Uploaded'}
        # print(uploaded_file.name)
        # print(uploaded_file.size)
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
    return render(request, '../templates/components/tables/tables.html', context=parameters)
