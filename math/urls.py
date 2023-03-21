from django.urls import path

from . import views


app_name = 'math'
urlpatterns = [
    path('triangle/', views.triangle, name='triangle')
]