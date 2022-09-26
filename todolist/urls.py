from django.urls import path
from todolist.views import todolist_mainpage
from todolist.views import todolist_login
from todolist.views import todolist_register
from todolist.views import todolist_createTask
from todolist.views import todolist_logout
from todolist.views import todolist_changeIsFinished
from todolist.views import todolist_deleteTask

app_name = 'todolist'

urlpatterns = [
    path('', todolist_mainpage, name='todolist_mainpage'),
    path('login/', todolist_login, name='todolist_login'),
    path('register/', todolist_register, name='todolist_register'),
    path('create-task/', todolist_createTask, name='todolist_createTask'),
    path('logout/', todolist_logout, name='todolist_logout'),
    path('changeIsFinished/<int:pk>', todolist_changeIsFinished, name='todolist_changeIsFinished'),
    path('deleteTask/<int:pk>', todolist_deleteTask, name='todolist_deleteTask'),
]