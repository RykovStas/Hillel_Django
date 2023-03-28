from django.shortcuts import render
from .models import User as UserModel


def show_persons(request):
    users = UserModel.objects.all()
    return render(request, "user/persons.html", {'users': users})
# Create your views here.
