# Tugas 6 PBP Qaniah Zahirah

### Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
Asynchronous programming proses jalannya dapat dilakukan secara bersamaan tanpa harus menunggu antrian. Klien tidak diblokir ketika suatu operasi sedang berjalan.
Synchronous proses jalannya secara sequential, berdasarkan antrian eksekusi program. Klien akan diblokir sampai operasi yang dijalankan selesai.

### Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Event-Driven Programming adalah ketika aliran dari program ditentukan oleh peristiwa (event). Peristiwa ini dapat berupa klik tombol, keluaran sensor, dan pembacaan output.
Contoh Event-Driven-Programming pada tugas ini ialah `$("#add-task").click(function()` yaitu akan ada beberapa perintah yang berjalan ketika diklik tombol untuk menambahkan task/submit.

### Jelaskan penerapan asynchronous programming pada AJAX.
Dengan AJAX, data dapat diperbaharui tanpa memuat ulang halaman web. Dengan begitu aktivitas yang sedang dilakukan tidak berhenti sampai response diberikan. Dapat dilihat pada program ini tidak dilakukan reload pada browser ketika menambahkan task baru dan task baru langsung ditampilkan.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
Membuat view baru pada file views.py yang mengembalikan seluruh data task dalam bentuk JSON.
```python
def show_json(request):
    data = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

Membuat path pada file urls.py dengan `path('json/', show_json, name='show_json'),`.

Mengambil task menggunakan AJAX GET pada file todolist.html.
```javascript
$.get("/todolist/json", function(data) {
            console.log(data)
            for (i=0; i < data.length; i++){
              $(".content").append(`<div class="row row-cols-1 row-cols-md-3 g-4">
                <div class="col">
                <div class="card">
                <div class="card-body">
                  <h5 class="card-title">${data[i].fields.title}</h5>
                  <p class="card-text">${data[i].fields.date}</p>
                  <p class="card-text">${data[i].fields.description}</p>
                </div>
                </div>
                </div>
              </div>`)
            }
          });
```
Membuat tombol Add New Task yang membuka modal.
```html
<button type="button" class="btn btn-secondary" data-bs-toggle="modal" data-bs-target="#exampleModal" data-bs-whatever="@mdo">Add New Task</button>
```

Membuat view baru untuk menambahkan task baru ke dalam database.
```python
@csrf_exempt
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        task = Task.objects.create(title=title, description=description,date=datetime.date.today(), user=request.user)

        result = {'fields':{'title':task.title,'description':task.description, 'date':task.date,},'pk':task.pk}
        return JsonResponse(result)
```

Membuat path pada file urls.py dengan `path('add/', add_task, name='add_task')`.

Menggunakan AJAX POST untuk menampilkan data baru yang diinput di file todolist.html
```javascript
$.post("{% url 'todolist:add_task' %}", {
            title: $('#title').val(),
            description: $('#description').val()}, 
            function (result){
              console.log("cbcb")
              $(".content").append(`<div class="row row-cols-1 row-cols-md-3 g-4">
                <div class="col">
                <div class="card">
                <div class="card-body">
                  <h5 class="card-title">${result.fields.title}</h5>
                  <p class="card-text">${result.fields.date}</p>
                  <p class="card-text">${result.fields.description}</p>
                </div>
                </div>
                </div>
              </div>`)
              $('#title').val(''),
              $('#description').val('')
            }
            )
```
Menutup modal dengan kode `data-bs-dismiss="modal"` di tombol submit.

Refresh secara asinkronus tanpa me-reload browser akan dilakukan untuk menampilkan todolist terbaru.
