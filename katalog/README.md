# Link menuju aplikasi Heroku
Berikut merupakan link menuju aplikasi Heroku [Lab 1 Qaniah](https://qaniapp-lab1.herokuapp.com/katalog/)

# Jawaban pertanyaan

## 1.
![Bagan Lab 1](https://user-images.githubusercontent.com/90833585/190292293-193261c3-7306-4e31-bda8-eb10e9d23b5f.png)

Permintaan user diteruskan ke urls.py yang kemudian diteruskan ke views.py untuk memilih tampilan web yang akan ditampilkan. Di dalam views.py terdapat elemen-elemen yang nantinya akan disisipkan ke dalam HTML. Lalu views.py akan meminta resource yang dibutuhkan ke models.py. Ketika ada permintaan yang melibatkan database, views.py akan memanggil query yang akan dikembalikan oleh database melalui models.py. Setelah permintaan terpenuhi, elemen-elemen akan diteruskan oleh views.py ke HTML. HTML itu kemudian ditampilkan kembali ke user.

## 2.
Virtual environment digunakan karena proyek memiliki kebutuhan yang berbeda-beda atas satu dengan yang lainnya. Dengan fungsinya yang ditujukan untuk memisahkan pengaturan dan package yang diinstal pada setiap proyek, virtual environment digunakan agar perubahan yang dilakukan pada satu proyek tidak mempengaruhi proyek lainnya. Jadi, dengan menggunakan virtual environment kita tidak perlu mengubah configurations pada sistem operasi yang kita pakai ketika menjalankan suatu proyek. 
Kita tetap dapat membuat aplikasi Web berbasis Django tanpa menggunakan virtual environment dan proyek tetap dapat berjalan. Akan tetapi, karena fungsi virtual environment yang ditujukan untuk memisahkan pengaturan dan package yang diinstal pada setiap proyek, proyek yang kita buat tanpa menggunakan virtual environment akan memiliki pengaturan dan package yang menyatu. 

## 3.
Cara saya mengimplementasikannya yaitu pertama dengan meng-clone repository template yang telah disediakan. Lalu saya meng-import models dari class katalog ke views.py. Kemudian, saya mengimplementasikan fungsi pada views.py yang dapat melakukan pengambilan data dari models.py dan dikembalikan ke dalam sebuah HTML yaitu dengan memanggil fungsi query ke model database, lalu disimpan ke sebuah variabel. Kemudian ditambahkan parameter ketiga pada return fungsi yang telah dibuat yang merupakan variabel berisi data tadi.
Kemudian agar halaman HTML dapat ditambilkan di browser, dibuat routing terhadap fungsi tersebut, yaitu dengan mendaftarkan katalog pada variabel urlpatterns. 
Lalu dilakukan iterasi menggunakan for loop pada variabel list_barang yang telah di-render ke dalam HTML.
Untuk melakukan deployment ke Heroku, pertama saya melakukan add, commit, dan push. Kemudian saya menyalin API key lalu menghubungkannya ke Github. Lalu saya menambahkan variabel repository secret dan menyimpan variabel-variabel tersebut. Kemudian saya membuka GitHub Actions dan menjalankan kembali workflow yang gagal hingga deployment menjadi sukses.