from django.test import TestCase, Client
from django.urls import resolve

class MyWatchListAppTest(TestCase):
    
    def test_show_watchlist_html_url_is_exist(self):
        response = Client().get('/mywatchlist/html', follow=True)
        self.assertEqual(response.status_code,200)

    def test_show_watchlist_xml_url_is_exist(self):
        response = Client().get('/mywatchlist/xml', follow=True)
        self.assertEqual(response.status_code,200)

    def test_show_watchlist_json_url_is_exist(self):
        response = Client().get('/mywatchlist/json', follow=True)
        self.assertEqual(response.status_code,200)