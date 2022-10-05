## [Tautan aplikasi Heroku todolist](https://tugas2-johannessetiawan.herokuapp.com/todolist/)

### Apa kegunaan ```{% csrf_token %}``` pada elemen ```<form>```? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen ```<form>```?
```{% csrf_token %}``` berguna untuk mengecek asal _form_ yang dikirim pengguna supaya pengguna tidak mengirim _form_ yang bukan berasal dari _website_ kita. Potongan kode tersebut berguna untuk menghindari CSRF _attacks_ pada _website_ kita. Jika tidak ada potongan kode tersebut, _form_ dari luar bisa masuk ke website kita sehingga pengguna bisa saja mengirimkan jawaban ke _form_ yang bukan dari _website_ kita tetapi dari orang luar yang memasukkan _form_-nya ke _website_ kita atau dengan kata lain pengguna tersebut bisa terkena CSRF _attacks_.
 
### Apakah kita dapat membuat elemen ```<form>``` secara manual (tanpa menggunakan generator seperti ```{{ form.as_table }}```)? Jelaskan secara gambaran besar bagaimana cara membuat ```<form>``` secara manual.
Ya. Caranya adalah dengan mendefinisikan ```action``` dan ```method``` pada tag ```<form>``` di _file_ HTML kita. Setelah itu membuat elemen ```<table>``` di dalam elemen ```<form>``` tersebut. Tabel tersebut bisa kita isi dengan elemen ```<input>``` sebagai tempat pengguna untuk meng-_input_ jawaban untuk _form_ kita. Kita bisa mendefinisikan ```name```, ```placeholder```, ```value```, dan ```type``` dari ```<input>``` tersebut. Untuk membuat suatu _button_ untuk _submit form_, kita bisa membuat ```<input>``` dengan ```type=”submit”```. 

### Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada _database_, hingga munculnya data yang telah disimpan pada _template_ HTML.
Pertama-tama, pengguna melakukan submisi _form_ yang diisi di _browser_. Setelah itu, _browser_ membuat HTTP _request_ yang diterima oleh _server_. _Server_ akan mencari fungsi di ```views.py``` yang meng-_handle_ _path_ dari _form_ tersebut. Setelah itu, fungsi tersebut akan mengambil informasi yang dimasukkan pengguna ke _form_ dengan _method_ ```.get()``` pada objek ```request.POST``` (bisa juga ```request.GET``` tergantung dengan ```method``` yang didefinisikan pada _form_ yang bersangkutan) yang masuk ke fungsi tersebut. Fungsi akan membuat objek baru di _database_ dengan _method_ ```NamaModel.objects.create(...)``` berdasarkan informasi yang dimasukkan untuk menyimpan data yang sudah dimasukkan pengguna ke _database_. Data tersebut akan disimpan ke dalam _database_ sebagai objek dari model NamaModel. Setelah proses tersebut selesai, _server_ akan membuat halaman HTML yang menampilkan data dari objek tersebut sesuai dengan _template_ yang didefinisikan dan kembalikan ke _browser_ sebagai _response_ dari _request_ yang dibuat. Halaman HTML tersebut berserta _data_ yang di-_submit_ pengguna akan tampil di _browser_ milik pengguna.
  
### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

1. Melakukan ```python manage.py startapp todolist``` untuk membuat aplikasi baru bernama ```todolist`` di proyek tugas Django yang sebelumnya. 
2. Menambahkan ```'todolist',``` pada ```INSTALLED_APPS``` di _file_ ```settings.py``` dan ```path('todolist/', include('todolist.urls')),``` pada ```urlpatterns``` di _file_ ```urls.py``` di _folder_ ```project_django```.
3. Membuat model ```Task``` dengan mengisi ```models.py``` di folder ```todolist``` dengan baris di bawah. Class ```Task``` yang dibuat memiliki 5 atribut, yaitu ```user``` berupa ```models.ForeignKey``` dengan parameter ```User```, ```date``` berupa ```DateTimeField``` yang akan diisi secara otomatis saat suatu objek dengan model ```Task``` dibuat, ```title``` berupa ```TextField```, ```description``` berupa ```TextField```, dan ```is_finished``` berupa ```BooleanField``` dengan nilai awalnya adalah ```False```.
```
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add = True)
    title = models.TextField()
    description = models.TextField()
    is_finished = models.BooleanField(default=False)
```
4. Membuat 7 fungsi di ```views.py``` aplikasi ```todolist```. Fungsi ```todolist_mainpage(request)``` berguna untuk menampilkan halaman _to do list_ dari pengguna yang _login_. Fungsi tersebut memiliki fungsi ```@login_required(login_url='/todolist/login/')``` yang membuat suatu pengguna harus _login_ terlebih dahulu sebelum melihat halaman _to do list_. Fungsi ```todolist_login(request)``` berguna untuk menampilkan _form_ halaman _login_ untuk pengguna. Fungsi ```todolist_register(request)``` berguna untuk menampilkan halaman _form_ registrasi untuk pengguna. Fungsi ```todolist_createTask(request)``` berguna untuk menampilkan _form_ pengguna untuk menambahkan sebuah _task_ baru. Fungsi ```todolist_logout(request)``` berguna _untuk menampilkan halaman _form_ registrasi untuk_logout_ pengguna dari aplikasi _todolist_. Fungsi ```todolist_changeIsFinished(request, pk)``` berguna untuk mengubah keterangan progres _task_ pengguna menjadi Selesai atau Belum Selesai. Fungsi ```todolist_deleteTask(request, pk)``` berguna untuk pengguna saat menghapus sebuah _task_.
5. Membuat _template_ halaman HTML untuk fungsi ```todolist_login(request)```, ```todolist_mainpage(request)```, ```todolist_register(request)```, dan ```todolist_createTask(request)```. 
6. _Template_ ```todolist_mainpage.html``` adalah halaman utama untuk menampilkan _to do list_ yang dibuat oleh pengguna yang _login_. Fungsi ```todolist_mainpage(request)``` akan mem-_filter_ objek ```Task``` yang nilai atribut penggunanya tidak sesuai dengan pengguna yang _login_. Setelah daat di-_filter_, ambil _username_ pengguna yang _login_ lalu di-_render_ dengan _template_ ini dan ditampilkan ke pengguna. Halaman ini memiliki tombol ```Tambah Task Baru``` untuk pengguna menambahkan _task_ baru ke dalam _to do list_-nya. Saat ditekan, halaman akan berpindah ke halaman untuk membuat _task_. Halaman ini juga memiliki tombol ```Logout`` yang akan menjalankan fungsi ```todolist_logout(request)``` yang membuat pengguna tersebut _logout_ dari aplikasi dan memindahkan halaman ke halaman _login_.
7. _Template_ ```login.html``` adalah halaman _form_ untuk _login_ pengguna yang meminta keterangan _username_ dan _password_ pengguna. Setelah pengguna menekan tombol ```Login```, data yang dimasukkan pengguna akan diproses oleh fungsi ```todolist_login(request)``` yang akan memvalidasi pengguna. Jika ada pengguna dengan _username_ dan _password_ yang dimasukkan, maka fungsi ini akan menampilkan halaman _to do list_ dari pengguna tersebut. Jika pengguna memencet link ```Buat Akun```, maka halaman akan berpindah ke halaman registrasi.
8. _Template_ ```createTask.html``` adalah halaman _form_ untuk pengguna membuat _task_ yang meminta judul dan deskripsi _task_ dari pengguna. Setelah pengguna menekan tombol ```Buat Task```, data yang dimasukkan pengguna akan diproses oleh fungsi ```todolist_createTask(request)``` yang akan membuat objek ```Task``` baru dengan judul dan deskripsi yang dimasukkan dan penggunanya adalah pengguna yang membuat _task_ tersebut. Setelah itu, objek tersebut dimasukkan ke _database_ dan halaman akan berpindah ke halaman _to do list_ dari pengguna tersebut yang menampilkan semua _task_ yang dibuat pengguna tersebut_.
9. Mengisi ```urls.py``` pada _folder_ ```todolist```  dengan isi di bawah ini sehingga semua fungsi yang ada di ```views.py``` bisa diakses melalui URL.
```
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
```
10. Melakukan ```push``` ke GitHub untuk melakukan _deployment_ ke aplikasi Heroku.
11. Membuat dua akun pengguna dan 3 objek dari model ```Task``` pada akun masing-masing di aplikasi Heroku. Pengguna pertama yang dibuat adalah ```akun1``` dengan _password_ ```johannessetiawan1```. Objek ```Task``` yang dimiliki pengguna pertama adalah Dummy1, Dummy2, dan Dummy4. Pengguna kedua yang dibuat adalah ```Akun2``` dengan _password_ ```johannessetiawan2```. Objek ```Task``` yang dimiliki pengguna kedua adalah Dummy3, Dummy5, dan Dummy6.


## TUGAS 5

### Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
Inline --> Dibuat dengan menambahkan atribut ```style``` di dalam tag sebuah elemen HTML. Kelebihannya adalah setiap elemen _style_-nya bisa berbeda-beda. Kelemahannya adalah kita harus mendefinisikannya di setiap elemen kecuali elemen yang _parent_-nya memiliki _inline style_. Selain itu, kita jadi sulit untuk mengatur _style_ dari halaman HTML kita dan struktur _file_ HTML kita jadi berantakan.

Internal --> Dibuat dengan elemen ```<style>``` di bagian ```<head>```. Kelebihannya adalah kita bisa memilih elemen mana saja yang ingin kita _style_ dengan mendefinisikan _selector_ untuk _element_, _class_, dan/atau _ID_ yang ada di dalam elemen ```<style>``` ke elemen tersebut. Kelemahannya adalah kita harus mendefiniskan ```<style>``` tersebut di setiap dokumen HTML kita. Selain itu, metode ini juga menambah ukuran _file_ HTML kita dan menambah _loading time_.

Eksternal --> Dibuat dengan elemen ```<link>``` berisi link yang menunjuk ke file eksternal CSS. Kelebihannya adalah kita mudah untuk menggunakan _style_ yang sama untuk semua dokumen HTML kita dengan memasukkan _link_ CSS yang menunjuk ke _file_ CSS yang sama dan ukuran _file_-nya lebih kecil. Kelemahannya adalah halaman HTMl kita tidak akan ter-_render_ penuh sebelum _external file_ CSS kita di-_load_ dan mengunduh _file_ dari berbagai _link_ dapat menambah _download time_ dari _website_ kita. 

### Jelaskan tag HTML5 yang kamu ketahui.

- ```<nav>``` --> Mendefinisikan kumpulan dari _links_. _Links_ yang ada di dalam elemen ini biasanya berupa navigasi menu utama pada halaman _website_.
- ```<header>``` --> Digunakan untuk mendefinisikan bagian dari halaman HTML yang berupa _header_ yang biasanya berada pada bagian atas web.
- ```<footer>``` --> Digunakan untuk mendefinisikan bagian dari halaman HTML yang berupa _footer_ yang biasanya berada pada bagian atas web.
- ```<article>``` --> Digunakan untuk memberi penanda bahwa suatu konten dapat berdiri sendiri tanpa terikat dengan konten lain.
- ```<section>``` --> Digunakan untuk mendefinisikan bagian/_section_ dalam sebuah dokumen HTML.

### Jelaskan tipe-tipe CSS selector yang kamu ketahui.

- _Element Selector_ --> Selektor yang memilih elemen berdasarkan jenis _tag_.
- _Class Selector_ --> Selektor yang memilih elemen berdasarkan nama _class_ yang didefiniskan pada tag elemen tersebut.
- _ID Selector_ --> Selektor yang memilih elemen berdasarkan nama _id_ yang didefiniskan pada tag elemen tersebut. Selektor ini hanya dapat digunakan satu kali.
- _Attribute Selector_ --> Selektor yang memilih elemen berdasarkan atribut yang didefinisikan di dalam elemen tersebut.
- _Universal Selector_ --> Selektor yang memilih semua elemen berdasarkan _scope_/jangkauan tertentu

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Menambahkan ```<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">``` ke setiap _head_ dari setiap dokumen HTML di folder ```templates``` supaya bisa menggunakan Bootstrap pada setiap dokumen. Bootstrap sudah otomatis membuat semua halaman _website_ yang dihasilkan menjadi _responsive_.
2. Menambahkan elemen ```<style>``` untuk menggunakan CSS pada ```login.html```,```createTask.html```, ```register.html```, dan ```todolist_mainpage.html```. Lalu membuat _style_ untuk setiap dokumen. _Style_ yang ditambahkan adalah _background_, _border_, _text alignment_, _color_, membuat komponen menjadi berada di tengah, dan sebagainya. Selain itu, _navbar_ juga dibuat pada halaman ```todolist_mainpage.html```.
3. Menambahkan elemen _card_ pada ```todolist_mainpage.html``` dengan kode sebagai berikut:
```
<div class="col-sm-3">
       <div class="card bg-warning" style="width: 18rem;">
         <div class="card-body">
           <h5 class="card-title">Judul: {{task.title}}</h5>
           <h6 class="card-subtitle mb-2 text-muted">Tanggal Pembuatan: {{task.date}}</h6>
           <p class="card-text">Deskripsi: {{task.description}}</p>
           <p class="card-text"> Selesai?
           {% if task.is_finished %}
                Selesai
                {% else %}
                Belum Selesai
                {% endif%}
           </p>
           <a href="{% url 'todolist:todolist_changeIsFinished' task.id %}" class="btn btn-primary">Ganti Progres</a>
           <a href="{% url 'todolist:todolist_deleteTask' task.id %}" class="btn btn-primary">Hapus Task</a>
         </div>
       </div>
      </div>
    {% endfor %}
    </div>
 ```
