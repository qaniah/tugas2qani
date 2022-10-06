# Tugas 5 PBP Qaniah Zahirah

### Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
#### Perbedaan
Inline CSS kodenya ditulis langsung pada atribut elemen HTML. Inline CSS ditulis pada setiap elemen HTML yang memiliki atribut style. Inline CSS digunakan hanya untuk mengubah satu elemen saja.
Internal CSS kodenya ditulis dalam tag <style> dan kode HTML ditulis pada header file HTML. Jika menggunakan internal CSS, tampilannya pada satu halaman website saja tidak digunakan pada halaman website yang lain. Dengan begitu, internal CSS cocok digunakan ketika ingin membuat halaman web dengan dengan tampilan yang berbeda pada setiap halaman websitenya.
External CSS kodenya ditulis terpisah dengan kode HTML. Terdapat file khusus yang berekstensi .css untuk menggunakan external CSS. File external ini diletakkan setelah bagian <head> pada halaman.
##### Kelebihan dan kekurangan
###### Inline
Kelebihan: Berguna untuk memperbaiki kode dengan cepat, proses load website lebih cepat, berguna ketika hanya ingin menguji dan melihat perubahan pada satu elemen.
Kekurangan: Tidak efisien karena hanya dapat diterapkan pada satu elemen HTML.
###### Internal
Kelebihan: Perubahannya hanya pada satu halaman saja, HTML dan CSS ada di satu file jadi tidak perlu melakukan upload beberapa file, internal stylesheet dapat menggunakan class dan ID.
Kekurangan: Tidak efisien ketika ingin menggunakan CSS yang sama pada beberapa file, load website lama. 
###### External
Kelebihan: Dapat digunakan di beberapa halaman web sekaligus, proses load website lebih cepat, ukuran file HTML menjadi lebih kecil.
Kekurangan: Ketika CSS gagal dipanggil oleh file HTML halaman akan menjadi berantakan.

### Jelaskan tag HTML5 yang kamu ketahui.
Tag HTML5 yang saya tau yaitu <! DOCTYPE> untuk mendefinisikan dokumennya, <html> untuk membuat halaman html, <head> untuk mendefinisikan informasi import CSS, import font, dan lain-lain, <title> untuk membuat judul pada suatu halaman, <body> untuk membuat bagian tubuh pada suatu halaman, <h1> to <h6> untuk membuat heading pada suatu halaman, <p> untuk membuat teks ukuran default pada suatu halaman, <div> untuk merepresentasikan suatu section, <table> untuk membuat table pada halaman, <button> untuk membuat tombol pada suatu halaman, <nav> untuk membuat navigation bar pada suatu halaman, dan masih banyak lagi tag lainnya.

### Jelaskan tipe-tipe CSS selector yang kamu ketahui.
Tipe CSS selector yang saya tau yaitu selector class yang ditulis dengan "." di depannya. Selector ini memilih elemen berdasarkan nama class yang diberikan. Lalu Selector ID yang ditulis dengan "#" di depannya. Selector ID ini bersifat unik dan hanya dapat digunakan pada satu elemen saja. Kemudian selector element yang ditulis disesuaikan dengan tag HTML yang ingin diberi style, tidak menggunakan "." maupun "#".

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
Menambahkan bootstrap ke setiap file html pada folder templates seperti yang sudah dilakukan pada tutorial 4 contohnya:
```html
<!doctype html>
 <html lang="en">
   <head>
     <meta charset="utf-8">
     <meta name="viewport" content="width=device-width, initial-scale=1">
     <title>Todolist</title>
     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
   </head>
```

Kemudian saya melakukan styling dengan inline CSS jadi saya langsung menulis kodenya pada setiap atribut elemen HTMLnya. Saya sangat terbantu dengan dokumentasi yang diberikan pada lab. Saya juga menambahkan navigation bar pada todolist.html yang memiliki warna sama dengan background halaman. Di dalam navigation bar itu saya memasukkan gambar, tulisan, dan button logout. Di halaman login, create-task, dan register implementasinya cukup mirip yaitu dengan menggunakan row. 


Lalu juga mengubah halaman todo list agar tasknya ada pada card yaitu dengan:
```html
<div class="row row-cols-1 row-cols-md-3 g-4">
    {% for todo in list_todo %}
      <div class="col">
        <div class="card">
        <div class="card-body">
          <h5 class="card-title">{{todo.title}}</h5>
          <h6 class="card-subtitle mb-2 text-muted">Date Created: {{todo.date}}</h6>
          <p class="card-text">{{todo.description}}</p>
        </div>
        </div>
      </div>
      {% endfor %}
    </div>  
```
Untuk responsivenya saya terbantu oleh penggunaan bootstrap karena telah tersedia fitur responsiveness.