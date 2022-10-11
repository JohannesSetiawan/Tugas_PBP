from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.core import serializers
from django.urls import reverse
from todolist.models import Task
from django.views.decorators.csrf import csrf_exempt


@login_required(login_url='/todolist/login/')
def todolist_mainpage(request):
    tasklist = Task.objects.filter(user=request.user)
    username = request.user.get_username()
    context = {
        'username': username,
        'tasklist': tasklist,
    }
    return render(request, "todolist_mainpage.html", context)

@login_required(login_url='/todolist/login/')
def show_json(request):
    data = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='/todolist/login/')
def buat_task_ajax(request):
    response_data = {}

    if request.POST.get('action') == 'post':
        judul = request.POST.get('judul')
        deskripsi = request.POST.get('deskripsi')
        user = request.user
        obj_baru = Task(user = user, title = judul, description = deskripsi)
        obj_baru.save()

        return JsonResponse({"instance": "Proyek Dibuat"},status=200)

def todolist_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:todolist_mainpage"))
            response.set_cookie('last_login', str(datetime.datetime.now())) 
            return response
        else:
            messages.info(request, 'Username atau password salah!')
    context = {}
    return render(request, 'login.html', context)

def todolist_register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Selesai membuat akun!')
            return redirect('todolist:todolist_login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def todolist_createTask(request):
    if request.method == 'POST':
        judul = request.POST.get('judul')
        deskripsi = request.POST.get('deskripsi')
        user = request.user
        Task.objects.create(user = user, title = judul, description = deskripsi)
        response = HttpResponseRedirect(reverse("todolist:todolist_mainpage"))
        return response

    return render(request, 'createTask.html')

def todolist_logout(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:todolist_login'))
    response.delete_cookie('last_login')
    return response

def todolist_changeIsFinished(request, pk):
    task = Task.objects.get(id=pk)
    task.is_finished = not(task.is_finished)
    task.save()
    return redirect('todolist:todolist_mainpage')
    
@csrf_exempt
def todolist_deleteTask(request, pk):
    if request.method == 'DELETE':
        Task.objects.filter(id=pk).delete()
    return JsonResponse({"instance": "Task Dihapus"},status=200)