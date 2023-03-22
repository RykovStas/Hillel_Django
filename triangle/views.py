from django.shortcuts import render, HttpResponse
from .forms import Calc
import math


def gipo(request):

    a = None
    b = None

    result = None

    if 'submit' in request.GET:
        gipo = Calc()
        if gipo.is_valid():
            result = (gipo.cleaned_data['a']^2 + gipo.cleaned_data['b']^2) ** 0.5
            gipo = Calc()
    else:
        gipo = Calc()
    return render(request, 'triangle/gipo.html', {'calc_form': gipo})
