from django.urls import path


from . import views


app_name = 'user'
urlpatterns = [
    path('', views.index, name='person'),
    path('show_persons/', views.show_persons, name='show_persons'),
    path('post_person/', views.post_person, name='register_user'),
    path('update_person/<int:pk>/', views.person_update, name='person_update'),
]