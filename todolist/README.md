# Tugas 4 PBP Qaniah Zahirah

## Link Heroku
Link App Heroku:
[Tugas 4 Qaniah Zahirah 2106639491](https://qaniapp-lab1.herokuapp.com/todolist/)

## Jawaban Pertanyaan
### Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
Guna dari {% csrf_token %} ialah untuk melindungi dari serangan CSRF (Cross Site Request Forgeries). Serangan ini merupakan serangan yang dapat terjadi pada aplikasi website kita berupa pengiriman form yang bukan dari server asli. Jika tidak ada potongan kode tersebut pada elemen <form> akan muncul error karena CSRF token tidak dapat ditemukan. Dengan begitu, halaman HTML tidak bisa diakses.

### Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
Bisa, yaitu dengan membuat <form> secara manual terlebih dahulu kemudian dibuat <label> sebagai penanda input apa yang akan dimasukkan lalu <input> sebagai input fieldsnya yang dapat berupa text, password, checkbox, radio button, atau lainnya. Perlu diperhatikan bahwa value dan atribut name pada input ini harus sama dengan kode di server Django.

### Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
Pertama-tama browser akan membuat HTTP Request, method, dan argumen yang diterima dari submisi pengguna ke destinasi URL berdasarkan HTML page form. Lalu server akan menerima HTTP Request tersebut dan mengecek apakah request yang dikirimkan valid. Setelah itu server memilih method pada views.py yang cocok untuk meng-handle request dari pengguna. Responnya kemudian diberikan dengan mengembalikan HTTP Response dan memproses data menjadi halaman HTML yang ditampilkan kepada pengguna

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Dengan command python3 manage.py startapp todolist kemudian juga menaruh todolist di INSTALLED_APPS pada settings.py yang ada di project_django.
2. Menambahkan path('todolist/', include('todolist.urls')), di urlpatterns pada urls.py di project_django dan path('', show_todolist, name='show_todolist'), di urlpatterns pada urls.py yang dibuat di folder todolist.
3. Membuat model Task pada models.py dengan kode sebagai berikut:
```python
    class Task(models.Model):
        user = models.ForeignKey(
            User, 
            on_delete=models.CASCADE,
        )
        date = models.DateField()
        title = models.CharField(max_length=250)
        description = models.TextField()
```
4. Menaruh kode-kode fungsi registrasi, login, dan logout sesuai dengan tutorial 3 pada views.py di folder todolist. Tidak lupa menaruh @login_required(login_url='/todolist/login/') di atas fungsi show_todolist agar diperlukan login ketika mengakses halaman.
5. Membuatnya pada todolist.html sesuai dengan tampilan yang diminta yaitu memuat username pengguna, tombol Tambah Task Baru, tombol logout, serta tabel berisi tanggal pembuatan task, judul task, dan deskripsi task.
6. Membuatnya pada createtask.html sesuai dengan tampilan yang diminta yaitu input dari judul dan deskripsi task.
7. Menaruh path-pathnya pada urlpatterns yang ada di urls.py pada folder todolist.
8. Dengan hanya melakukan add, commit, dan push akan otomatis ter-deploy karena sebelumnya telah dilakukan deploy pada repository ini.
9. Akun-akunnya yaitu:
```
Username: qani  Password: ayatoxiao
Username: jennie  Password: blackpink
```