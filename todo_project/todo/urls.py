from django.urls import path
from . import views


urlpatterns =[
    path('', views.task_list, name='task_list'),
    path('task/create/', views.task_create, name='task_create'),
]

# After defining the app routes. take urlspattern and register them to the project
