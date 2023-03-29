from django.urls import path


from . import views


app_name = 'user'
urlpatterns = [
    path('', views.index, name='person'),
    path('show_persons/', views.show_persons, name='show_persons'),

]