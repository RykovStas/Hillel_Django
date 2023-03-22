from django.shortcuts import render, HttpResponse
from .forms import Calc
import math

def gipo(request):
    result = None
    if 'Submit' in request.GET:
        user_form = Calc(request.GET)

        if user_form.is_valid():
            a = user_form.cleaned_data['a']
            b = user_form.cleaned_data['b']
            result = math.sqrt(a*a + b*b)

            user_form = Calc()
    else:
        user_form = Calc()
    return render(request, 'triangle/gipo.html', {'calc_form': user_form, 'result': result})
