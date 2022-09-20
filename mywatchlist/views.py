from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from mywatchlist.models import MyWatchList

def show_watchlist_main(request):
    data_watchlist = MyWatchList.objects.all()
    already_watched = 0
    not_watched = 0
    for film in data_watchlist:
        if film.watched == "Yes":
            already_watched+=1
        if film.watched == "No":
            not_watched+=1
    message = "Wah, kamu masih sedikit menonton!"
    if already_watched >= not_watched:
        message = "Selamat, kamu sudah banyak menonton!"
    context = {
        'nama': 'Johannes Setiawan',
        'npm': '2106750345',
        'already_watched': already_watched,
        'not_watched': not_watched,
        'message' : message
    }
    return render(request, "mainpage.html", context)

def show_watchlist_html(request):
    data_watchlist = MyWatchList.objects.all()
    context = {
        'watch_list': data_watchlist,
        'nama': 'Johannes Setiawan',
        'npm': '2106750345'
    }
    return render(request, "watchlist.html", context)

def show_watchlist_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_watchlist_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
