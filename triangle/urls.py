from django.urls import path, include

from . import views


app_name = 'triangle'
urlpatterns = [
    path('', views.gipo, name='gip')
]