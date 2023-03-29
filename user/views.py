from django.shortcuts import render, redirect, get_object_or_404
from .models import User as UserModel
from .forms import PersonForm


def index(request):
    return render(request, 'user/index.html', {})

def show_persons(request):
    users = UserModel.objects.all()
    return render(request, "user/persons.html", {'users': users})


def post_person(request):
    if request.method == "POST":
        user_form = PersonForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('user:show_persons')
    else:
        user_form = PersonForm()

    return render(request, 'user/post_person.html', {'form': user_form})


def person_update(request, pk):
    obj = get_object_or_404(UserModel, pk=pk)
    if request.method == 'POST':
        user_form = PersonForm(request.POST, instance=obj)
        if user_form.is_valid():
            obj = user_form.save()
            return redirect('triangle:person')
    else:
        user_form = PersonForm(instance=obj)

    return render(request, 'user/person_update.html', {'form': user_form, 'obj': obj})
