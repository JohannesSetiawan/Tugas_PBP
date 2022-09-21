## [Tautan aplikasi Heroku](https://tugas2-johannessetiawan.herokuapp.com/mywatchlist/)

### Jelaskan perbedaan antara JSON, XML, dan HTML!
HTML --> Bahasa marka standar yang digunakan untuk menampilkan suatu dokumen pada halaman web. HTML tidak bisa digunakan untuk menyimpan data. HTML dibangun dengan komponen yang disebut _HTML elements_. _HTML elements_ memiliki _tag_ tertentu untuk mendeskripsikan elemen tersebut. _HTML elements_ dapat memiliki _attribute_ sebagai informasi tambahan dari elemen tersebut. Terdapat _empty elements_ yang terdiri dari 1 _tag_ tanpa _closing tag_. HTML bersifat _case-insensitive_.

XML --> XML adalah bahasa marka yang biasa digunakan untuk menyimpan dan mengirimkan data. XML menyimpan data dalam format teks sederhana sehingga data mudah dibaca oleh _server_. XML juga _self-descriptive_ sehingga data mudah dimengerti oleh manusia. Struktur dokumen XML berbentuk seperti pohon/_tree_ dengan _root element_ sebagai elemen yang wajib ada pada suatu dokumen XML. XML tidak memiliki _tag_ tertentu sehingga kita harus membuat tag kita sendiri. Setiap elemen XML harus mempunyai _closing tag_. _Tag_ pada XML _case-sensitive_.

JSON --> JSON adalah suatu format yang digunakan untuk menyimpan dan mengirimkan data. JSON memiliki struktur yang sederhana dan mudah untuk dipahami. Data disimpan dalam pasangan _name/value_ dan kumpulan data tersebut digunakan untuk membuat objek. Setiap objek dipisahkan dengan tanda kruung kurawal. JSON memiliki fungsi yang sama dengan XML, tetapi memiliki beberapa keunggulan seperti ukuran _file_ yang lebih kecil sehingga proses _load data_ lebih cepat, struktur kode yang lebih sederhana sehingga proses penulisan kode lebih cepat, dan kode lebih ringkas sehingga mudah dipahami.

### Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
_Data delivery_ diperlukan dalam pengimplementasian sebuah platform supaya data yang ada di dalam basis data _server_ bisa ditampilkan dan dilihat oleh _qlient_ sebagai pengguna platform. _Data delivery_ juga diperlukan untuk melakukan transfer/pertukaran data dari satu basis data ke basis data lain.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

1. Membuat aplikasi ```mywatchlist``` dengan perintah ```python manage.py startapp mywatchlist``` 
2. Menambahkan ```path('mywatchlist/', include('mywatchlist.urls')),``` ke dalam ```urlpatterns``` yang ada di _folder_ ```aplikasi_django``` untuk melakukan _routing_ terhadap fungsi ```views.py``` aplikasi ```mywatchlist``` sehingga halaman HTML yang ada di _folder_ templates pada _folder_ aplikasi ```mywatchlist``` bisa ditampilkan di web.
3. Mengisi models.py aplikasi mywatchlist dengan membuat sebuah _class_ ```MyWatchList``` dengan atribut ```watched```, ```title```, ```rating```, ```release_date```, dan ```review``` sebagai berikut:
```
class MyWatchList(models.Model):
    watched = models.TextField()
    title = models.TextField()
    rating = models.IntegerField()
    release_date = models.TextField()
    review = models.TextField()
```
4. Jalankan perintah ```python manage.py makemigrations``` lalu perintah ```python manage.py migrations``` untuk mempersiapkan dan menerapkan skema model yang sudah dibuat pada models.py ke basis data aplikasi ```mywatchlist``` yang ada di Django.
5. Membuat sebuah _folder_ bernama ```fixtures```. Setelah itu membuat sebuah _file_ bernama ```data_watchlist.json``` pada _folder_ tersebut. Menambahkan 11 data film dengan atribut yang sesuai dengan atribut yang dimiliki _class_ ```MyWatchList``` ke dalam _file_ tersebut. Data yang ditambahkan adalah sebagai berikut:
```
[
    {
        "model":"mywatchlist.mywatchlist",
        "pk":1,
        "fields":{
            "watched":"No",
            "title":"Fall",
            "rating": "3",
            "release_date": "August 12, 2022",
            "review": "Fundamentally absurd yet as evocatively minimalist as its title, Fall is a sustained adrenaline rush for viewers willing to suspend disbelief."
        }
},
{
        "model":"mywatchlist.mywatchlist",
        "pk":2,
        "fields":{
            "watched":"No",
            "title":"God's Country",
            "rating": "4",
            "release_date": "September 16, 2022",
            "review": "Led by an outstanding Thandiwe Newton, God's Country rewards patient viewers with a slow-burning but ultimately explosive story of inexorable conflict."
        }
},
{
        "model":"mywatchlist.mywatchlist",
        "pk":3,
        "fields":{
            "watched":"Yes",
            "title":"Top Gun: Maverick",
            "rating": "5",
            "release_date": "May 27, 2022",
            "review": "Top Gun: Maverick pulls off a feat even trickier than a 4G inverted dive, delivering a long-belated sequel that surpasses its predecessor in wildly entertaining style."
        }
},
{
        "model":"mywatchlist.mywatchlist",
        "pk":4,
        "fields":{
            "watched":"No",
            "title":"Elvis",
            "rating": "4",
            "release_date": "August 9, 2022",
            "review": "The standard rock biopic formula gets all shook up in Elvis, with Baz Luhrmann's dazzling energy and style perfectly complemented by Austin Butler's outstanding lead performance."
        }
},
{
        "model":"mywatchlist.mywatchlist",
        "pk":5,
        "fields":{
            "watched":"Yes",
            "title":"Moonage Daydream",
            "rating": "5",
            "release_date": "September 16, 2022",
            "review": "An audiovisual treat for Bowie fans, Moonage Daydream takes an appropriately distinctive approach to one of modern music's most mercurial artists."
        }
},
{
        "model":"mywatchlist.mywatchlist",
        "pk":6,
        "fields":{
            "watched":"No",
            "title":"Confess, Fletch",
            "rating": "4",
            "release_date": "September 16, 2022",
            "review": "Shorter on wacky hijinks but still very funny, Confess, Fletch is a showcase for Jon Hamm's comedic chops that revives this long-dormant franchise with style."
        }
},
{
        "model":"mywatchlist.mywatchlist",
        "pk":7,
        "fields":{
            "watched":"Yes",
            "title":"Nope",
            "rating": "4",
            "release_date": "July 12, 2022",
            "review": "Admirable for its originality and ambition even when its reach exceeds its grasp, Nope adds Spielbergian spectacle to Jordan Peele's growing arsenal."
        }
},
{
        "model":"mywatchlist.mywatchlist",
        "pk":8,
        "fields":{
            "watched":"Yes",
            "title":"Barbarian",
            "rating": "5",
            "release_date": "September 9, 2022.",
            "review": "Smart, darkly humorous, and above all scary, Barbarian offers a chilling and consistently unpredictable thrill ride for horror fans."
        }
},
{
        "model":"mywatchlist.mywatchlist",
        "pk":9,
        "fields":{
            "watched":"Yes",
            "title":"Pearl",
            "rating": "4",
            "release_date": "September 16, 2022",
            "review": "Pearl finds Ti West squeezing fresh gore out of the world he created with X -- and once again benefiting from a brilliant Mia Goth performance."
        }
},
{
        "model":"mywatchlist.mywatchlist",
        "pk":10,
        "fields":{
            "watched":"No",
            "title":"Happening",
            "rating": "5",
            "release_date": "May 6, 2022",
            "review": "A tough but rewarding watch, Happening puts a personal face on an impossibly difficult choice and its heart-rending aftermath."
        }
},
{
        "model":"mywatchlist.mywatchlist",
        "pk":11,
        "fields":{
            "watched":"No",
            "title":"The Woman King",
            "rating": "5",
            "release_date": "September 16, 2022",
            "review": "All hail Viola Davis! The Woman King rules."
        }
}
]
```
6. Menjalankan perintah ```python manage.py loaddata data_watchlist.json``` untuk memasukkan data yang ada di dalam ```data_watchlist.json``` ke dalam basis data Django lokal milik aplikasi ```mywatchlist```.
7. Mengimplementasi fungsi ```views.py``` untuk menyajikan 11 data tersebut ke dalam 3 format, yaitu HTML, XML, dan JSON, dan menampilkan halaman utama dari aplikasi ```mywatchlist```. Isi dari fungsi ```views.py``` adalah sebagai berikut:
```
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from mywatchlist.models import MyWatchList

# Create your views here.
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
```
Fungsi ```show_watchlist_main``` digunakan untuk menampilkan halaman utama aplikasi. Fungsi ```show_watchlist_html``` digunakan untuk menampilkan data ke dalam format HTML. Fungsi ```show_watchlist_xml``` digunakan untuk menampilkan data ke dalam format XML. Fungsi ```show_watchlist_json``` digunakan untuk menampilkan data ke dalam format JSON.

8. Membuat _folder_ ```templates``` di _folder_ aplikasi ```mywatchlist```. Buat dua _file_ HTML di _folder_ tersebut. _File_ ```mainpage.html``` digunakan sebagai _template_ halaman utama aplikasi. _File_ ```watchlist.html``` digunakan sebagai _template_ untuk menampilkan data dalam format HTML.
9. Membuat _file_ ```urls.py``` di _folder_ aplikasi ```mywatchlist``` untuk membuat _routing_ sehingga 11 data bisa diakses ke dalam format HTML, XML, dan JSON pada halaman web. Buat juga _routing_ untuk halaman utama aplikasi. Isi dari urls.py adalah sebagai berikut:
```
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
```
11. Melalukan ```git pull```, ```add```, ```commit```, dan ```push``` ke dalam repositori GitHub untuk melakukan _deployment_ terhadap aplikasi ```mywatchlist``` yang sudah dibuat ke Heroku.

### Gambar Postman
HTML:

![HTML](https://github.com/JohannesSetiawan/Tugas_PBP/blob/main/mywatchlist/gambar/html.png)

XML:

![XML](https://github.com/JohannesSetiawan/Tugas_PBP/blob/main/mywatchlist/gambar/xml.png)

JSON:

![JSON](https://github.com/JohannesSetiawan/Tugas_PBP/blob/main/mywatchlist/gambar/json.png)
