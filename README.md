# Tugas 3
## 1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Jawaban :
Data delivery atau pengiriman data sangat penting dalam implementasi platform karena platform harus berinteraksi dengan pengguna dan sistem lain melalui sebuah data :
- **Interaksi dengan pengguna** : Data delivery memastikan bahwa komunikasi terjadi secara efisien karena pengguna mengirimkan dan menerima data terus menerus.
- **Sinkronisasi data antar sistem** : Platform bergantung pada integrasi dengan sistem eksternal seperti API pihak ketiga atau layanan cloud. Data delivery memastikan adanya sinkronisasi antara platform dan sistem lain berjalan lancar.
- **Pengambilan keputusan Real-Time** : Platform membutuhkan data yang dikirim secara real-time untuk memberi respon langsung pada pengguna.
- **Keamanan dan privasi** : Data delivery mencakup pengiriman data yang aman. Menggunakan metode eknripsi yang baik memastikan bahwa data sampai tanpa resiko kebocoran atau penyalahgunaan.
- **Pengelolaan skala besar** : Platform besar harus menangani sejumlah pengiriman data dalam jumlah besar dari jutaan pengguna atau perangkat. Data delivery yang efisien memastikan bahwa platform dapat beroperasi dengan baik dibawah beban tinggi

## 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Jawaban : 
JSON(JavaScript Object Notation) lebih populer daripada XML(Extensible Markup Language) karena beberapa alasan :
- **Sintaksis** pada JSON lebih padat dan lebih mudah dibaca serta ditulis dibandingkan dengan XML yang mengganti beberapa karakter untuk referensi entitas sehingga jauh lebih rumit daripada JSON.
- **Ukuran** JSON umumnya lebih ringkas karena tidak memerlukan tag penutup berulang '<tag></tag>' seperti XML sehingga menghemat bandwith dan mempercepat transfer data
- **Kecepatan parsing** JSON dirancang untuk bisa mengolah lebih cepat di browser modern, karena JSON langsung kompatibel dengan object JavaScript. Proses parsing JSON lebih cepat dibanding XML di sebagian besar *environment*, terutama dalam aplikasi web
- **Kemanan** JSON lebih aman dibandingkan dengan XML sedangkan pada XML pengguna harus mematikan DTD ketika bekerja dengan XML untuk memitigasi potensi risiko keamanan

Namun, XML masih digunakan dalam beberapa kasus tertentu, misalnya untuk:

- Validasi Data yang Kuat: XML memiliki kemampuan untuk validasi data yang kuat menggunakan DTD (Document Type Definition) atau XML Schema, yang lebih kompleks dibandingkan dengan JSON.
- Dokumen Markup: XML sering digunakan untuk markup dokumen yang kompleks, seperti dalam aplikasi yang memerlukan pengaturan format dokumen atau data yang terstruktur dengan aturan yang lebih ketat (misalnya, dalam dokumen HTML atau SOAP).

Secara keseluruhan, JSON lebih populer karena jauh lebih cepat, ringan, dan cocok untuk digunakan aplikasi web modern, sedangkan XML lebih sering digunakan dalam konteks yang memerlukan markup yang lebih kaya dan validasi yang ketat

## 3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Jawaban :
Method is_valid() pada form Django berfungsi untuk memvalidasi input data dan memastikan bahwa data yang dimasukkan sesuai dengan aturan validasi yang ditentukan di form
- Memvalidasi input data : is_valid() untuk memeriksa apakaha data yang diinput pengguna sudah memenuhi syarat validasi yang didefinisikan pada form seperti tipe data, format email yang valid, maksimum karakter, dll
- Menandai field yang invalid : Jika terdapat data yang tidak valid maka is_valid() akan mengembalikan False dan otomatis menampilkan pesan kesalahan ke form 

Lalu mengapa kita butuh is_valid()?
- Untuk memastikan integritas data : memastikan bahwa data yang diproses atau disimpan di database sudah bersih dan valid, hal ini untuk mencegah data yang rusak atau tidak sesuai format masuk ke dalam sistem
- Keamanan aplikasi : memvalidasi data yang sangat penting untuk menghindari potensi eksploitasi seperti serangan SQL Injection atau Cross-Site Scripting (XSS), yang bisa terjadi jika input tidak divalidasi dengan baik 
- Penangan form yang sederhana : dengan is_valid(), validasi form dapat dikelola secara otomatis oleh Django, tanpa perlu memeriksa data satu per satu secara manual. Ini mempermudah penanganan form dan menjaga kode tetap bersih dan mudah dipelihara.


## 4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
Jawaban :
CSRF atau Cross-Site Request Forgery adalah jenis serangan yang memaksa pengguna untuk melakukan tindakan yang tidak diinginkan pada aplikasi web yang sudah terautentikasi. csrt_token ini berguna untuk melindungi aplikasi Django dari serangan CSRF. 

Mengapa kita butuh csrf_token? 
csrf_token adalah token keamanan untuk melindungi aplikasi dari serangan CSRF. Hal ini untuk memastikan bahwa request yang dibuat oleh server benar-benar berasal dari pemiliki yang sah bukan eksternal lain yang jahat. Django secara otomatis menghasilkan token CSRF yang unik untuk tiap sesi pengguna dan memasukkannya ke form HTML. Token ini harus dikirim bersama data dorm saat pengguna mengirim request POST. Jika token valid, maka request ianggap aman. jika tidak, request akan ditolak.

Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django?
Jika form Django tidak memiliki csrf_token, maka Django akan **rentan terhadap serangan CSRF**. Penyerang bisa saja memanfaatkan sesi yang sudah aktif (login) untuk mengubah kata sandi, hapus akun tanpa sepengetahuan pengguna. 

Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
Penyerang bisa menggunakan teknik mengirim link berbahaya melalui email atau media sosial untuk mengarahkan korban ke halaman yang membuka akses untuk memicu permintaan otomatis ke aplikasi web yang di targetkan. Kedua, penyerang bisa membuat form tersembunyi di situs mereka yang mengirimkan permintaan POST ke aplikasi web di mana pengguna sudah terautentikasi. Penyerang juga bisa memanfaatkan gambar atau iframe yang mengarahkan ke URL tersebut dan melancarkan aksi.

Pada intinya, csrf_token berfungsi sebagai pelindung aplikasi web dari serangan CSRF yang dapat merugikan pengguna seperti kehilangan akun, password yang diganti tanpa sepengetahuan pengguna, transaksi yang tidak diingiinkan, pengubahan data dan masih banyak lagi


## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Jawaban :
1. Pertama, buat folder/direktori 'templates' pada root utama folder dan buat berkas 'base.html'. Berkas ini berfungsi sebagai template dasar untuk kerangka umum untuk halaman web (tampilan utama) pada proyek yang sedang dibuat. Dalam file ini terdapat baris-baris yang berfungsi untuk membuat data secara dinamis dari Django ke HTML.
2. Kemudian, buka  'settings.py' pada direktori amolali_bakery, tambahkan kode untuk baris 'DIRS' menjadi "'DIRS': [BASE_DIR / 'templates']," agar file base.html terdeteksi sebagai template
3. Buka folder main/templates, kemudian ubah kode pada file 'main.html' menjadi seperti ini utnuk extend file 'base.html':
{% extends 'base.html' %}
{% block content %}

<h1> Amolali Bakery </h1>

<h5>NPM: </h5>
<p>{{ npm }}<p>

<h5>Name:</h5>
<p>{{ name }}</p>

<h5>Class:</h5>
<p>{{ class }}</p>
{% endblock content %}

4. Ubah primary key dari integer menjadi UUID, import uuid pada file 'models.py' menjadi seperti ini :
import uuid #tambahkan baris ini di paling atas
from django.db import models

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # tambahkan baris ini juga
    name = models.CharField(max_length=255)  # Atribut nama product
    price = models.IntegerField()  # Atribut harga product
    description = models.TextField()  # Atribut deskripsi product
    category = models.CharField(max_length=100, blank=True, null=True)  # Atribut kategori product
    image = models.URLField()  # Atribut gambar product

    def __str__(self):
        return self.name
image = models.URLField(), field ini untuk menambahkan gambar menggunakan link yang berasal dari internet 

5. Kemudian lalukan migration dan migrate menggunakan perintah :
python3 manage.py makemigrations
python3 manage.py migrate

6. Buat form untuk input data dan menampilkan product yang sudah ditambahkan pada form input data. Buat file baru pada folder main dengan nama 'forms.py', tambahkan kode berikut :
from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "category", "image"]

7. Buka file 'views.py' lalu tambahkan import :
from django.shortcuts import render, redirect #Tambahkan import redirect di baris ini
from main.forms import ProductForm
from main.models import Product

buatlah fungsi untuk menerima parameter request :
def create_product_entry(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)

sesuaikan baris kode pada fungsi show_main untuk mengambil seluruh objek Product yang tersimpan di database : 
def show_main(request):
    product_entries = Product.objects.all()

8. Buka file 'urls.py' pada folder/direktori 'main' kemudian import fungsi create_product_entry menjadi :
from main.views import show_main, create_product_entry
9. Tambahkan path URL ke dalam variabel urlpatterns di 'urls.py' di folder 'main'
urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product_entry, name='create_product'),
]
10. Buat file baru yang saya beri nama 'create_product.html' di folder/direktori main/templates
{% extends 'base.html' %} 
{% block content %}
<h1>Add New Product</h1>

<form method="POST">
  {% csrf_token %}
  <table>
    {{ form.as_table }}
    <tr>
      <td></td>
      <td>
        <input type="submit" value="Add Product" />
      </td>
    </tr>
  </table>
</form>

{% endblock %}

11. Buka file 'main.html' lalu tambahkan kode ini di dalam {% block content %} untuk menampilkan data product ke dalam bentuk tabel dan menampilkan tombol 'Add New Product'
....
{% if not product_entries %}
<p>Belum ada data product pada amolali bakery.</p>
{% else %}
<table>
  <tr>
    <th>Product Name</th>
    <th>Price</th>
    <th>Image</th>
    <th>Category</th>
    <th>Description</th>
  </tr>

  {% comment %} Berikut cara memperlihatkan data product di bawah baris ini 
  {% endcomment %} 
  {% for product in product_entries %}
  <tr>
    <td>{{product.name}}</td>
    <td>{{product.price}}</td>
    <td><img src="{{product.image}}" alt="{{product.name}}" style="width: 200px; height: 200px;"></td>
    <td>{{product.category}}</td>
    <td>{{product.description}}</td>
  </tr>
  {% endfor %}
</table>
{% endif %}

<br />

<a href="{% url 'main:create_product' %}">
  <button>Add New Product</button>
</a>

{% endblock content %}

'<td><img src="{{product.image}}" alt="{{product.name}}" style="width: 200px; height: 200px;"></td>'
    <td>{{product.category}}</td>, baris kode ini berfungsi untuk menampilkan link foto menjadi foto yang diinginkan pada tampilan halaman utama

10. Kemudian, jalankan Django dengan perintah 'python3 manage.py runserver' dan akses dengan link http://localhost:8000/ untuk mencoba mulai menambahkan product

11. Buat kode untuk mengembalikan data dalam bentuk XML 
    - Buka file 'views.py' pada folder/direktori 'main' dan tambahkan import :
        from django.http import HttpResponse
        from django.core import serializers
    - Buat fungsi baru untuk menerima parameter show_xml
        def show_xml(request):
            data = Product.objects.all()
            return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    - Buka file 'urls.py' pada folder main lalu import fungsi yang dibuat tadi :
        from main.views import show_main, create_product_entry, show_xml
    - Tambahkan path url nya ke urlpatterns:
        ...
        path('xml/', show_xml, name='show_xml'),
        ...
    - Jalankan proyek Django dengan perintah 'python3 manage.py runserver' dan buka dengan link http://localhost:8000/xml/

12. Buat kode untuk mengembalikan data dalam bentuk JSON
    - Buat fungsi baru untuk menerima parameter show_xml
        def show_json(request):
            data = Product.objects.all()
            return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    - Buka file 'urls.py' pada folder main lalu import fungsi yang dibuat tadi :
        from main.views import show_main, create_product_entry, show_xml, show_json
    - Tambahkan path url nya ke urlpatterns:
        ...
        path('json/', show_json, name='show_json'),
        ...
    - Jalankan proyek Django dengan perintah 'python3 manage.py runserver' dan buka dengan link http://localhost:8000/json/

13. Buat kode untuk mengembalikan data menggunakan ID dalam bentuk XML ataupun JSON
    - untuk XML :
        def show_xml_by_id(request, id):
            data = Product.objects.filter(pk=id)
            return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    - untuk JSON:
        def show_json_by_id(request, id):
            data = Product.objects.filter(pk=id)
            return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    - Buka file 'urls.py' pada folder main lalu import fungsi yang dibuat tadi :
        from main.views import show_main, create_product_entry, show_xml, show_json, show_xml_by_id, show_json_by_id
    - Tambahkan path url nya ke urlpatterns:
        ...
        path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
        path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
        ...
    - Jalankan proyek Django dengan perintah 'python3 manage.py runserver' dan buka dengan link http://localhost:8000/xml/[id]/ ataupun http://localhost:8000/json/[id]/, masukkan id proyek yang ingin ditampilkan didalam kotak id '[id]'

14. Untuk mengakses menggunakan Postman sebagai Data viewer cukup ikuti langkah ini :
    - Pastikan server sudah berjalan dengan perintah 'python3 manage.py runserver'.
    - Buka Postman dan buatlah sebuah request baru dengan method GET dan url http://localhost:8000/xml/ atau http://localhost:8000/json/ untuk mengetes apakah data terkirimkan dengan baik.
    - Klik tombol Send untuk mengirimkan request tersebut.
    - Hasilnya dapat dilihat seperti pada screenshot dibawah ini mencari menggunakan tampilan XML, JSON, atau menggunakan ID dalam bentuk XML ataupun JSON


## Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
- format xml :
![](https://github.com/salsaaruum/amolali_bakery/blob/main/ScreenshotXML_SalsabilaArumdapta.png)

- format json :
![](https://github.com/salsaaruum/amolali_bakery/blob/main/ScreenshotJSON_SalsabilaArumdapta.png)

- format xml dengan id :
![](https://github.com/salsaaruum/amolali_bakery/blob/main/ScreenshotXML_ID_SalsabilaArumdapta.png)

- format json dengan id :
![](https://github.com/salsaaruum/amolali_bakery/blob/main/ScreenshotJSON_ID_SalsabilaArumdapta.png)




# Tugas 2
## 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Jawaban :
- Pertama saya membuat direktori/folder di lokal berjudul "amolali_bakery"
- Kemudian saya membuat repositori baru di Github dengan judul "amolali_bakery"
- Selanjutnya saya melakukan konfigurasi awal git dengan memasukkan kalimat "git init" pada terminal folder lokal
- Masukkan seluruh konfigurasi pengguna dan email, kemudian verifikasi konfigurasi 
- Selanjutnya buat branch utama dengan perintah "git branch -M main"
- Hubungkan folder/direktori lokal dengan repositori Github dengan perintah "git remote add origin https://github.com/salsaaruum/amolali_bakery.git"
- Selanjutnya lakukan instalasi Django dan insiasi Django, pada terminal yang sama jalankan perintah "python3 -m venv env"
- Kemudian aktifkan virtual environment dengan menjalankan perintah "source env/bin/active"
- Siapkan berkas requirements.txt lalu install dengan perintah "pip install -r requirements.txt", kemudian buat proyek Django "Django-admin startproject amolali_bakery ."
- Lakukan konfigurasi dan jalankan server dengan menambahkan string pada file settings.py "ALLOWED_HOSTS = ["localhost", "127.0.0.1"]"
- Kemudian jalankan server Django dengan melakukan perintah "python3 manage.py runserver"
- Cek, jika sudah muncul animasi rocket pada http://localhost:8000, maka aplikasi Django sudah berhasil dibuat
- Klik ctrl + C pada keyboard untuk mematikan virtual environment
- Buat berkas ".gitignore" untuk menentukan berkas dan direktori mana yang harus diabaikan oleh Git
- Kemudian saya lakukan add, commit, dan push
- Aktifkan virtual environment dengan perintah yang sama dengan sebelumnya kemudian jalankan perintah "python3 manage.py startapp main"
- Tambahkan string "main" pada berkas settings.py "INSTALLED_APPS = ['main']"
- Buat folder/direktori baru pada aplikasi 'main' dengan nama "templates" kemudian buat file baru dengan judul "main.html" isi sesuai kebutuhan untuk tugas ini
- Cek apakah berkas file "main.html" dapat dibuka di peramban web dengan cara double click
- Lalu ubah berkas models.py pada aplikasi main sesuai dengan kebutuhan dengan nama class "Product" sesuai ketentuan tugas
- Lakukan migrasi model dengan perintah "python3 manage.py makemigrations" kemudian lakukan migrasi ke dalam basis data lokal dengan perintah "python3 manage.py migrate"
- Buka file views.py pada aplikasi 'main' lalu tambahkan fungsi show_main dan saya sesuaikan dengan tugas saya
- Buka file "main.html" dan modifikasi dengan sintaks Django untuk menampilkan nilai dari variabel yang sudah didefinisikan
- Lakukan konfigurasi routing dengan cara membuat berkas "urls.py" di dalam folder main lalu tambahkan "include" untuk menghubungkan ke tampilan main
- Jalankan lagi proyek Django dengan perintah "python3 manage.py runserver" lalu cek apakah muncul animasi rocket pada "http://localhost:8000/" atau tidak
- Selamat proyek Tugas Individu 2 sudah selesai. Tidak lupa untuk melakukan add, commit, dan push untuk update isi repositori amolali_bakery pada Github 
- Tidak lupa untuk melakukan deploy pada PWS dengan cara yang sama seperti pada Github, yaitu dengan cara membuat proyek baru dengan menu "Create New Project"
- Masukkan nama project kemudian lakukan perintah pada project command PWS dengan mengatur remote, mengubah branch dari 'main' ke 'master' dan langkah terakhir lakukan perintah 'push pws master'
- Klik view project maka proyek yang dibuat sudah dapat dilihat


## 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
Jawaban:
![](https://github.com/salsaaruum/amolali_bakery/blob/main/BaganNomor2_SalsabilaArumdapta.jpg)
Penjelasan : Ketika klien mengirimkan permintaan ke Internet, permintaan tersebut diteruskan ke aplikasi Python/Django, lalu diarahkan ke 'urls.py' untuk pemetaan URL. Dari sana, permintaan diteruskan ke 'views.py' yang menangani logika untuk memproses URL tersebut. Selama proses ini, data dapat dibaca atau ditulis dari/ke 'models.py' dan database. Data yang diproses kemudian dikirimkan ke template untuk ditampilkan, dimana template tersebut digabungkan dengan nilai-nilai yang diinginkan. Hasil akhirnya adalah file HTML yang kemudian dikembalikan melalui Internet dan ditampilkan di perangkat klien.


## 3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
Jawaban:  
- Merekam / menyimpan perubahan kode : Git memungkinkan untuk merekam atau menyimpan setiap perubahan pada kode yang disimpan dalam bentuk commit sehingga memudahkan untuk melihat siapa yang melakukan perubahan, apa, dan kapan perubahan dilakukan
- Kolaborasi tim : Git memungkinkan beberapa pengembang kerja secara bersamaan pada proyek yang sama, terdapat fitur branching dan merging untuk kolaborasi yang lebih mudah dengan memisahkan perubahan yang sedang dikerjakan pada fitur tertentu sebelum digabung ke kode utama
- Penyimpanan terdistribusi : Git memiliki sistem yang terdistribusi, setiap perubahan tersimpan pada riwayat proyek. Pengembang bisa bekerja secara offline dan menyinkronkan perubahan saat kembali online.
- Mengembalikan kode ke versi sebelumnya : Jika terdapat masalah pada kode baru, pengembang dapat dengan mudah kembali ke versi kode sebelumnya. Tiap commit dapat diakses kapan saja sehingga mengurangi resiko terjadi bug atau kesalahan.
- Integrasi dengan CI/CD: Git sering digunakan bersama dengan alat Continuous Integration/Continuous Deployment (CI/CD), seperti GitHub Actions, GitLab CI, dan lainnya, untuk otomatisasi proses pengujian, pembangunan, dan deployment setelah perubahan dikirim ke repositori.


## 4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Jawaban:
- Bersifat "Batteries Included" : Django menyediakan fitur bawaan yang bisa digunakan tanpa memerlukan konfigurasi tambahan seperti autentikasi, pengelolaan database, pengiriman email sehingga memudahkan pemula menggunakannya dan fokus pada logika aplikasi
- Mengajarkan konsep pengembangan web :
    - MVT (Model View Template) : Membantu pemula memahami pemisahan antara data, logika bisnis, dan tampilan/interface
    - ORM (Object Relational Mapping) : Django menggunakan ORM untuk berinteraksi dengan datase sehingga pemula tidak perlu menulis quey SQL secara manual
    - Routing dan URL Mapping : Membantu untuk memahami dasar bagaimana URL dipetakan ke fungsi atau tampilan di aplikasi web
- Dokumentasi yang Komprehensif: Django memiliki dokumentasi yang sangat komprehensif dan ramah pemula. Dokumentasinya memberikan banyak contoh, penjelasan, dan panduan langkah demi langkah yang memudahkan pengguna baru untuk belajar secara mandiri.
- Terstruktur dan Scalable: Django memfasilitasi pengembangan aplikasi yang baik dan terstruktur sejak awal. Hal ini penting bagi pemula agar mereka belajar tentang pentingnya organisasi kode yang rapi, yang sangat berguna jika proyek tumbuh lebih besar dan kompleks.
- Memiliki keamanan bawaan seperti CSRF, SQL injection, dan XSS sehingga pemula tidak perlu khawatir dengan konfigurasi yang rumit terkait keamanan


## 5. Mengapa model pada Django disebut sebagai ORM?
Jawaban:
Model Django disebut sebagai ORM (Object Relation Mapping) karena memungkinkan pemetaan otomatis antara objek Python dan tabel dalam database relasional. Django ORM memberikan pengembang cara yang lebih mudah dan intuitif untuk bekerja dengan database, tanpa harus berurusan langsung dengan SQL query yang kompleks, serta mendukung struktur data berorientasi objek yang lebih konsisten dengan bahasa pemrograman Python.

## Link deploy PWS
https://salsabila-arumdapta-amolalibakery.pbp.cs.ui.ac.id
