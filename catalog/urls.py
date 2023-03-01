from django.urls import path

from catalog.views import start

urlpatterns = [
    path('', start, name='start')
]