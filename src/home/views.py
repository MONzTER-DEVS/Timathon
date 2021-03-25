from io import StringIO

import pandas as pd
import os
import openpyxl
import time
import matplotlib.pyplot as plt
import numpy as np

from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib import messages
from matplotlib.backends.backend_agg import FigureCanvasAgg

from timathon.settings import MEDIA_ROOT
from .forms import TableDataForm

# Create your views here.
table_data = []


# the home page
def index(request):
    return render(request, 'home/index.html')


# @login_required
def components(request):
    return render(request, 'components/components.html')


def favourites(request):
    return render(request, 'home/favourites.html')


def charts(request):
    return render(request, 'components/charts/charts.html')


def extract_data(fp):
    """

    :param fp: file name
    :return: data in that file
    """

    if fp.endswith('csv'):
        data = pd.read_csv(fp)

    elif fp.endswith('xls') or fp.endswith('xlsx'):
        data = pd.read_excel(fp)

    return data


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

            data = extract_data(fn)
            table_data.append(data)
            # time.sleep(2)
            return HttpResponseRedirect(reverse_lazy('home:table_results'))
        else:
            print('OOF')
    else:
        data = None
        form = TableDataForm()
    context = {"form": form}
    return render(request, 'components/tables/tables.html', context)


def table_result(request):
    try:
        messages.success(request, 'Your Data Has Been Successfully Analyzed By Mentis Oculi')
        headers = []
        for header in table_data[-1]:
            headers.append(header)
        context = {'data': table_data[-1], 'headers': headers}
    except Exception:
        context = {'data': []}
    return render(request, 'components/charts/select.html', context)


def charts_select(request):
    if request.method == 'GET':
        return render(request, "components/charts/select.html")
    elif request.method == 'POST':
        # file extraction not working


        # print(request.FILES)
        # file = request.FILES['file']
        #
        # type_of_chart = request.POST['type']
        # fn = os.path.join(MEDIA_ROOT, file.name)
        # data = extract_data(fn)

        # making the plot
        x = np.arange(0, np.pi * 3, .1)
        y = np.sin(x)
        fig = plt.figure()
        plt.plot(x, y)

        # converting
        imgdata = StringIO()
        fig.savefig(imgdata, format='svg')
        imgdata.seek(0)
        to_return_plot = imgdata.getvalue()

        context = {
            'graph': to_return_plot
        }

        return render(request, "components/charts/chart_rendered.html", context)
