# Link menuju aplikasi Heroku
Berikut merupakan link menuju aplikasi Heroku 
[Tugas 3 Qaniah Zahirah 2106639491](https://qaniapp-lab1.herokuapp.com/mywatchlist/)

# Jawaban Pertanyaan

## 1. 
Perbedaan antara JSON, XML, dan HTML:
1. JSON didesain menjadi self-describing, dengan begitu JSON sangat mudah untuk dimengerti. Format JSON berbentuk text. Data pada JSON disimpan dalam bentuk key and value.

2. XML didesain menjadi self-descriptive, dengan begitu ketika membaca XML kita dapat mengerti informasi apa yang ingin disampaikan dari data yang tertulis. Format XML berbentuk tag, yaitu informasinya dibungkus di dalam tag di mana kita harus menulis program untuk mengirim, menerima, menyimpan, atau menampilkan informasi. Dokumen XML membentuk struktur seperti tree yang dimulai dari root (harus ada), lalu branch, hingga berakhir pada leaves. 

3. HTML lebih menitikberatkan pada bagaimana format tampilan dari data. Format HTML berbentuk tag, namun tag-tag itu hanya mengatur bagaimana data dalam file itu akan ditampilkan, tidak ada informasi mengenai isi dari data tersebut.

## 2.
Diperlukan data delivery dalam pengimplementasian sebuah platform karena kita perlu mengirim data dari stack ke stack yang lain. Data yang dikirim tentunya dalam bermacam ragam, misalnya JSON, XML, dan HTML. Data-data tersebut dikirimkan melalui data delivery.

## 3.
Dibuat app mywatchlist dengan menggunakan command startapp. Lalu app tersebut ditambahkan ke dalam INSTALLED_APPS pada folder settings.py. 

Pertama dibuat fungsi pada file views.py. Lalu dibuat folder templates dan didalamnya diisi file html yang berisi data-data yang akan ditampilkan di website. Di file urls.py dilakukan routing dengan menambahkan path yaitu fungsi yang telah dibuat di views.py. Dengan begitu localhost akan dapat digunakan.

Ditambahkan class MyWatchList di file models.py yang ada di folder mywatchlist yang berisi atribut-atribut yang diinginkan. 

Di file pada folder fixtures saya menulis 10 data sesuai ketentuan soal. Lalu data diload ke database Django lokal.

Diimplementasi fungsi show_mywatchlist yang variabelnya memuat objek juga memiliki return value. Kemudian di file html dimunculkan datanya dengan looping. Jika program dijalankan akan muncul tabel.

Untuk mengembalikan data dengan bentuk html, xml, dan json, dibuat fungsi-fungsi baru pada file views.py. Di-import juga hal-hal yang diperlukan. Terdapat variabel yang mengandung objek datanya pada fungsi-fungsi tersebut. Di dalam file urls.py ditambahkan path url. Dengan begitu akan muncul kembalian file html/xml/json. 

Karena sudah dilakukan deploy sebelumnya, saya menambahkan kode pada Procfile lalu melakukan add commit dan push Dengan begitu akan muncul tampilan aplikasi mywatchlist pada Heroku.

# Screenshot Postman
![Screen Shot 2022-09-22 at 09 49 18](https://user-images.githubusercontent.com/90833585/191647596-6ab1d326-b947-4f87-b9e4-59278c2608c2.png)
![Screen Shot 2022-09-22 at 09 49 46](https://user-images.githubusercontent.com/90833585/191647664-cee426e3-154c-4718-be1a-a42ce3cc9f00.png)
![Screen Shot 2022-09-22 at 09 50 37](https://user-images.githubusercontent.com/90833585/191647772-e30929a0-7405-4f77-bad6-00235f0c8dfb.png)
