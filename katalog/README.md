# Link aplikasi Heroku: tugas2-johannessetiawan.herokuapp.com/katalog/

### 1.	Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html

Gambar bagan:
![Bagan](https://github.com/JohannesSetiawan/Tugas_PBP/blob/main/katalog/diagram%20tugas%202%20pbp.jpg)

Penjelasan bagan:

Pada bagan tersebut, _request_/permintaan yang masuk diteruskan ke ```urls.py```. ```urls.py``` memproses lalu meneruskan permintaan ke ```views.py``` yang sesuai dengan _request_ tersebut. Saat ada proses di ```views.py``` yang membutuhkan data dari _database_, ```views.py``` akan membuat suatu _query_ untuk meminta data ke ```models.py```. ```models.py``` mengambil data dari _database_ lalu dimodelkan. Setelah itu, data yang sudah dimodelkan tersebut dikirim ke ```views.py```. ```views.py``` mengirim data tersebut ke _templates_ untuk berkas html. Berkas html yang dihasilkan menjadi _responds_ ```views.py``` terhadap permintaan yang diterima.

### 2.	Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Kita menggunakan _virtual environment_ supaya kita tetap bisa membuka proyek Django kita di perangkat berbeda dengan versi Django yang berbeda. Selain itu, _virtual environment_ juga memisahkan proyek yang satu dengan proyek lain sehingga pengubahan yang dilakukan pada satu proyek tidak akan mengubah isi proyek lain. Namun, kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan _virtual environment_.

### 3.	Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.

1.	_Clone_ repositori template tugas lab lalu buka _directory_ repositori tersebut di command prompt

2.	Membuat fungsi yang mengambil data dari ```models.py``` dan dikembalikan menjadi sebuah html bernama ```katalog.html``` dengan mengubah isi _file_ ```views.py``` di dalam
    _folder_ katalog. Isi views.py diubah dengan menambahkan baris di bawah ini:
    ```
    def show_katalog(request):
        return render(request, "katalog.html")
    ```
3.	Mengisi _file_ ```urls.py``` pada _folder_ ```katalog``` untuk melakukan _routing_ yang memetakan fungsi ```views.py``` yg sudah dibuat. Isi dari ```urls.py``` pada _folder_ katalog adalah teks di bawah ini:
    ```
    from django.urls import path
    from katalog.views import show_katalog

    app_name = 'katalog'

    urlpatterns = [
        path('', show_katalog, name='show_katalog'),
    ]
    ```
4.	Menambahkan baris ```path('katalog/', include('katalog.urls'))``` pada ```urls.py``` yang ada di _folder_ ```project_django``` supaya aplikasi katalog dapat dibuka dan di-_deploy_.
5.	Menambahkan baris ```from katalog.models import CatalogItem``` pada ```views.py``` di _folder_ katalog untuk _import_ model yang sudah dibuat pada ```models.py``` ke views.py.
6.	Tambahkan baris di bawah ini pada fungsi ```show_katalog``` di dalam ```views.py``` di _folder_ ```katalog```.
    ```
    data_barang_katalog = CatalogItem.objects.all()
    context = {
        'list_barang': data_barang_katalog,
        'nama': 'Johannes Setiawan'
    }
    ````
7.	Tambahkan juga ```context``` sebagai parameter ketiga untuk fungsi ```render``` pada _return statement_ fungsi ```show_katalog``` sehingga menjadi ```return render(request, "katalog.html", context)```. Hal tersebut berguna untuk melakukan _render_ data dari model _database_ supaya data tersebut bisa ditampilkan pada berkas html setelah dilakukan pemetaan.
8.	Mengisi bagian ```nama``` dan ```student id``` pada _file_ ```katalog.html``` dan juga tambahkan baris di bawah ini setelah baris ```{% comment %} Add the data below this line {% endcomment %}``` untuk memetakan data yang ada ke _template_ html:
    ```
    {% for barang in list_barang %}
        <tr>
            <th>{{barang.item_name}}</th>
            <th>{{barang.item_price}}</th>
            <th>{{barang.description}}</th>
            <th>{{barang.item_stock}}</th>
            <th>{{barang.rating}}</th>
            <th>{{barang.item_url}}</th>
        </tr>
    {% endfor %}
    ```
9.	Mengubah isi ```urls.py``` bagian ```urlpatterns``` pada _folder_ ```project_django``` dengan menambahkan ```url``` untuk aplikasi katalog. Isi ```urlpatterns``` menjadi seperti di bawah ini:
    ```
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('example_app.urls')),
        path('katalog/', include('katalog.urls'),
    ]
    ```
10.	Men-_deploy_ aplikasi tersebut ke Heroku app dengan melakukan push ke github.
