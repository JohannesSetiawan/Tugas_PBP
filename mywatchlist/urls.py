from django.urls import path
from mywatchlist.views import show_watchlist_main
from mywatchlist.views import show_watchlist_html
from mywatchlist.views import show_watchlist_xml
from mywatchlist.views import show_watchlist_json

app_name = 'mywatchlist'

urlpatterns = [
    path('', show_watchlist_main, name='show_watchlist_main'),
    path('html/', show_watchlist_html, name='show_watchlist_html'),
    path('xml/', show_watchlist_xml, name='show_watchlist_xml'),
    path('json/', show_watchlist_json, name='show_watchlist_json'),
]