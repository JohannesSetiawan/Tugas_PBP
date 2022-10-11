from django.urls import path
from todolist.views import *

app_name = 'todolist'

urlpatterns = [
    path('', todolist_mainpage, name='todolist_mainpage'),
    path('json/', show_json, name='show_json'),
    path('add/', buat_task_ajax, name='buat_task_ajax'),
    path('login/', todolist_login, name='todolist_login'),
    path('register/', todolist_register, name='todolist_register'),
    path('create-task/', todolist_createTask, name='todolist_createTask'),
    path('logout/', todolist_logout, name='todolist_logout'),
    path('changeIsFinished/<int:pk>', todolist_changeIsFinished, name='todolist_changeIsFinished'),
    path('delete/<int:pk>', todolist_deleteTask, name='todolist_deleteTask'),
]