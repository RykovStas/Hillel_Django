from django.urls import path

from user.views import show_persons

urlpatterns = [
    path('', show_persons, name='persons')
]