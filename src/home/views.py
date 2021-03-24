import pandas as pd
import os
import openpyxl
import pprint
from django.shortcuts import render, redirect, reverse
from .forms import TableDataForm
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from timathon.settings import MEDIA_ROOT

# Create your views here.
table_data = []


# the home page
def index(request):
    return render(request, 'home/index.html')


@login_required
def components(request):
    return render(request, 'components/components.html')


def favourites(request):
    return render(request, 'home/favourites.html')


def charts(request):
    return render(request, 'components/charts/charts.html')


def read_excel(fp):
    wb = openpyxl.load_workbook(fp)
    sheet = wb.active
    num_of_columns = sheet.max_column
    num_of_rows = sheet.max_row

    all_rows = []
    for row in range(1, num_of_rows + 1):
        this_row = []
        for col in range(1, num_of_columns + 1):
            this_row.append(sheet.cell(row=row, column=col).value)

        all_rows.append(this_row)
    return all_rows


# def tables(request):
# parameters = {}
# if request.method == 'POST':
#     uploaded_file = request.FILES['datafile']
#     if uploaded_file.name.endswith('.csv'):
#         parameters = {'result': 'Correct File Uploaded'}
#     else:
#         parameters = {'result': 'Incorrect File Uploaded'}
#     # print(uploaded_file.name)
#     # print(uploaded_file.size)
#     fs = FileSystemStorage()
#     fs.save(uploaded_file.name, uploaded_file)
# return render(request, '../templates/components/tables/tables.html', context=parameters)


def tables(request):
    data = None
    if request.method == 'POST':
        form = TableDataForm(request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            fs = FileSystemStorage()
            fs.save(uploaded_file.name, uploaded_file)
            form.save()
            fn = os.path.join(MEDIA_ROOT, uploaded_file.name)
            if fn.endswith('csv'):
                data = pd.read_csv(os.path.join(MEDIA_ROOT, uploaded_file.name))

            elif fn.endswith('xls') or fn.endswith('xlsx'):
                raw = read_excel(fn)
                data = pd.DataFrame(raw)

            table_data.append(data)
            return HttpResponseRedirect(reverse_lazy('home:table_results'))
    else:
        data = None
        form = TableDataForm()
    context = {"form": form}
    return render(request, 'components/tables/tables.html', context)


def table_result(request):
    try:
        context = {'data': table_data[-1]}
    except Exception:
        context = {'data': []}
    return render(request, 'components/table_results/results.html', context)
