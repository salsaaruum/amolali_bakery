# Tugas 4
## 1. Apa perbedaan antara HttpResponseRedirect() dan redirect()?
Jawaban :
Perbedaan antara HttpResponseRedirect() dan redirect() di Django terletak pada tingkat abstraksi dan kemudahan penggunaanya:
- **HttpResponseRedirect()** :
    - Merupakan kelas bawaan Django yang mengirimkan respon HTTP untuk mengarahkan pengguna ke URL lain
    - Jika mneggunakan HttpResponseRedirect(), pengguna perlu menentukan URL secara manual
    - HttpResponseRedirect() berguna jika pengguna ingin mengontrol langsung bagaimana pengalihan atau ketika bekerja dengan URL yang sudah disiapkan sebelumnya

- **redirect()** :
    - Merupakan shortcut yang disediakan Django untuk memudahkan proses pengalihan. ini lebih fleksibel karena menerima berbagai jenis argumen : 
        - path URL string
        - nama dari view (dengan parameter untuk mnegisi argumen URL)
        - sebuah instance model (kemudian otomatis mengarahkan ke URL detailnya)
    - redirect() secara internal menggunakan HttpResponseRedirect() untuk membuat pengalihan, namun menyederhanakan beberapa hal untuk pengembang

## 2. Jelaskan cara kerja penghubungan model Product dengan User!
Jawaban :
Model product dengan user dihubungkan melalui ForeignKey atau relasi lain seperti ManyToManyField atau OneToOneField untuk mencatat siapa pembuat, siapa pemilik, atau pengelola produk tersebut. Berikut adalah cara kerjanya :
- **Model User**: Django sudah memiliki model pengguna bawaan, yaitu User, yang disediakan oleh django.contrib.auth.models. pengguna dapat mengimpor dan menggunakannya langsung dalam model.
- **Model Product**: Buat model Product yang berisi atribut-atribut produk, seperti name, price, dan description. Untuk menghubungkan produk dengan pengguna, pengguna dapat menggunakan ForeignKey.
- **Menggunakan ForeignKey** : ForeignKey digunakan untuk membuat relasi satu-ke-banyak, di mana satu pengguna dapat memiliki banyak produk, tetapi setiap produk hanya dimiliki oleh satu pengguna. Pengguna bisa menambahkan field ForeignKey dalam model Product yang merujuk ke user
- **Contoh penggunaanya**:
    from django.contrib.auth.models import User
    import uuid #tambahkan baris ini di paling atas
    from django.db import models

    class Product(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # tambahkan baris ini juga
        name = models.CharField(max_length=255)  # Atribut nama product
        price = models.IntegerField()  # Atribut harga product
        description = models.TextField()  # Atribut deskripsi product
        category = models.CharField(max_length=100, blank=True, null=True)  # Atribut kategori product
        image = models.URLField()  # Atribut gambar product

        def __str__(self):
            return self.name
"user = models.ForeignKey(User, on_delete=models.CASCADE)", ini membuat hubungan antara Product dengan User. Field User menyimpan referensi pengguna yang membuat/memiliki produk. "on_delete=models.CASCADE" artinya jika pengguna dihapus, maka semua produk yang terkait dengan pengguna juga akan dihapus
- **Mengakses Data**: Setelah model dihubungkan, Anda dapat dengan mudah mengakses produk yang dimiliki oleh pengguna tertentu, atau mengetahui siapa pemilik dari suatu produk :
     product_entries = Product.objects.filter(user=request.user), untuk mendapatkan semua produk yang dimiliki pengguna
    
## 3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
Jawaban :
Perbedaan antara authentication dan authorization, apakah yang dilakukan saat login:
    1. **Authentication**:
        - **Definisi** : Adalah proses verifikasi identitas seorang pengguna. Ini memastikan bahwa pengguna yang mengklaim suatu identitas (misalnya, dengan nama pengguna dan kata sandi) benar-benar memiliki hak tersebut
        - **Tujuan** : Memastikan bahwa pengguna adalah siapa yang mereka klaim
        - **Contoh apa yang terjadi** : Pengguna memasukkan username dan password untuk verifikasi. Jika kombinasi cocok, maka pengguna dianggap terautentikasi, jika tidak maka akses ditolak dan mengerlarkan pesan error
    2. **Authorization**:
        - **Definisi** : Adalah proses pemberian izin kepada pengguna untuk mengakses sumber daya atau melakukan tindakan tertentu setelah identitas mereka terverifikasi. Authorization terjadi setelah authentication
        - **Tujuan** : Memastikan pengguna yang terautentikasi hanya dapat mengakses sumber daya yang diizinkan
        - **Contoh apa yang terjadi** : Setelah login, pengguna memiliki izin melihat halaman profil, namun tidak diizinkan untuk mengakses halaman administrasi kecuali punya peran admin
Bagaimana Django mengimplementasikan kedua konsep tersebut:
    1. **Authentication di Django**:
     - Django menyediakan sistem autentikasi yang siap pakai di modul django.contrib.auth. Ini mencakup fitur login, logout, dan pengelolaan pengguna
        - Django memiliki fungsi authenticate() yang memverifikasi kredensial:
            from django.contrib.auth import authenticate
        - Login dan Logout: Setelah pengguna berhasil diautentikasi, Django menyimpan status login menggunakan sesi, terdapat fungsi logout() dan fungsi login() :
            from django.contrib.auth import authenticate, login, logout
            def login_user(request):
                if request.method == 'POST':
                    form = AuthenticationForm(data=request.POST)

            def logout_user(request):
                logout(request)
                response = HttpResponseRedirect(reverse('main:login'))
                response.delete_cookie('last_login')
                return response
===============================================================================
    2. **Authorization di Django**:
        - Permissions: Django memungkinkan Anda untuk menetapkan permissions untuk model atau tindakan tertentu. Misalnya, setiap model dalam Django secara otomatis mendapatkan tiga permission standar: add, change, dan delete
        - Groups: Django juga mendukung groups, yang merupakan cara untuk mengelompokkan beberapa pengguna dan memberikan izin secara kolektif 
        - Django's Decorators: Django juga menyediakan dekorator untuk memudahkan otorisasi di view

## 4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
Jawaban :
Django mengingat pengguna yang telah login dengan memanfaatkan cookies dan session framework. Ketika pengguna berhasil login, Django membuat session untuk pengguna tersebut dan menyimpan identifier session (session ID) di dalam cookie di browser pengguna. Setiap kali pengguna melakukan permintaan HTTP (seperti membuka halaman baru), session ID ini dikirim kembali ke server oleh browser, memungkinkan Django mengenali pengguna yang login. Contoh proses :
    from django.contrib.auth import authenticate, login, logout
    Ini akan menyimpan session ID di cookie dan mengaitkannya dengan session pengguna di server. Saat pengguna mengakses halaman lain, browser akan mengirimkan cookie yang berisi session ID, memungkinkan Django memeriksa session tersebut dan mengetahui bahwa pengguna telah login.

Kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
Selain untuk mengingat pengguna yang sudah login, cookies memiliki kegunaan lain:
- **Pelacakan Aktivitas**: Cookies dapat digunakan untuk melacak perilaku pengguna di website, seperti halaman yang dikunjungi atau barang yang dilihat, sehingga website dapat menampilkan rekomendasi yang relevan.
- **Menyimpan preferensi pengguna**: Cookies digunakan untuk menyimpan preferensi, seperti bahasa yang dipilih, tema, atau pengaturan tampilan, sehingga pengguna tidak perlu mengatur ulang setiap kali mengunjungi situs tersebut.
- **Analisis statistik**: Cookies membantu pemilik website memahami pola kunjungan dan perilaku pengguna, seperti berapa lama pengguna tinggal di halaman tertentu atau halaman mana yang paling sering dikunjungi, yang dapat digunakan untuk meningkatkan pengalaman pengguna.

Lalu apakah semua cookies aman untuk digunakan? **tidak semua cookies aman untuk digunakan**, ada beberapa pertimbangan keamanan terkait penggunaan cookies, terutama yang berkaitan dengan autentikasi dan privasi.


## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Jawaban :
1. **Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.** :
 - Buat fungsi registrasi :
    - Pastikan virtual environment sudah aktif (ada (env) di terminal)
    - Buka views.py lalu tambahkan import UserCreationForm dan messages :
        from django.contrib.auth.forms import UserCreationForm
        from django.contrib import messages
    - Tambahkan fungsi register di views.py :
        def register(request):
            form = UserCreationForm()

            if request.method == "POST":
                form = UserCreationForm(request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Your account has been successfully created!')
                    return redirect('main:login')
            context = {'form':form}
            return render(request, 'register.html', context)
    - Buat berkas berjudul register.html di folder templates:
        {% extends 'base.html' %}

        {% block meta %}
        <title>Register</title>
        {% endblock meta %}

        {% block content %}

        <div class="login">
        <h1>Register</h1>

        <form method="POST">
            {% csrf_token %}
            <table>
            {{ form.as_table }}
            <tr>
                <td></td>
                <td><input type="submit" name="submit" value="Daftar" /></td>
            </tr>
            </table>
        </form>

        {% if messages %}
        <ul>
            {% for message in messages %}
            <li>{{ message }}</li>
            {% endfor %}
        </ul>
        {% endif %}
        </div>

        {% endblock content %}

    - Buka file urls. py tambahkan import register : from main.views import register, kemudian tambahkan path url nya : 
         urlpatterns = [
            ...
            path('register/', register, name='register'),
        ]

- Buat fungsi Login
    - Buka file views.py, tambahkan import menjadi seperti ini :
        from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
        from django.contrib.auth import authenticate, login
    - Tambahkan fungsi login_user :
        def login_user(request):
            if request.method == 'POST':
                form = AuthenticationForm(data=request.POST)

                if form.is_valid():
                        user = form.get_user()
                        login(request, user)
                        return redirect('main:show_main')

            else:
                form = AuthenticationForm(request)
            context = {'form': form}
            return render(request, 'login.html', context)
    - Buat file berjudul login.html di folder templates :
        {% extends 'base.html' %}

        {% block meta %}
        <title>Login</title>
        {% endblock meta %}

        {% block content %}
        <div class="login">
        <h1>Login</h1>

        <form method="POST" action="">
            {% csrf_token %}
            <table>
            {{ form.as_table }}
            <tr>
                <td></td>
                <td><input class="btn login_btn" type="submit" value="Login" /></td>
            </tr>
            </table>
        </form>

        {% if messages %}
        <ul>
            {% for message in messages %}
            <li>{{ message }}</li>
            {% endfor %}
        </ul>
        {% endif %} Don't have an account yet?
        <a href="{% url 'main:register' %}">Register Now</a>
        </div>

        {% endblock content %}

    - Buka urls.py, tambahkan import : from main.views import login_user, kemudian tambahkan path url nya :
        urlpatterns = [
            ...
            path('login/', login_user, name='login'),
        ]

- Buat fungsi logout :
    - Buka file views.py, tambahkan import menjadi seperti ini :
    from django.contrib.auth import logout
    - Tambahkan fungsi logout_user ke dalam fungsi views.py:
        def logout_user(request):
            logout(request)
            return redirect('main:login')
    - Buka file main.html, tambahkan potongan kode ini dibawah hyperlink tag untuk Add New Product
    ...
    <a href="{% url 'main:logout' %}">
    <button>Logout</button>
    </a>
    ...
    - Buka urls.py, import fungsi yang dibuat tadi: from main.views import logout_user, lalu tambahkan path url nya menjadi seperti ini :
         urlpatterns = [
            ...
            path('logout/', logout_user, name='logout'),
        ]
selanjutnya restriksi akses ke halaman main :
- Buka views.py, import login_required:
    from django.contrib.auth.decorators import login_required
- Kemudian tambahkan potongan kode menjadi seperti ini:
    @login_required(login_url='/login') #tambahkan ini
    def show_main(request):
- Akses Djnago di link http://localhost:8000/ dengan menjalankan python3 manage.py runserver

2. **Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.** :
- Akun 1:
    ![](https://github.com/salsaaruum/amolali_bakery/blob/main/Screenshot_akun1.png)
- Akun 2:
    ![](https://github.com/salsaaruum/amolali_bakery/blob/main/Screenshot_akun2.png)

3. **Menghubungkan model Product dengan User** :
- Buka models.py, kemudian impor model : from django.contrib.auth.models import User
-  Pada model Product, tambahkan potongan kode :
    class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
- Buka views.py, ubah kode pada fungsi create_product_entry jadi :
    def create_product_entry(request):
        form = ProductForm(request.POST or None)

        if form.is_valid() and request.method == "POST":
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect('main:show_main')

        context = {'form': form}
        return render(request, "create_product.html", context)
- Ubah value pada fungsi show_main dari all menjadi filter dan ubah pada variabel name:
    def show_main(request):
    product_entries = Product.objects.filter(user=request.user)

    context = {
        'name': request.user.username,
        ...
    }
- Simpan semua perubahan dan lakukan migrasi
- Tetapkan default value untuk field user pada semua row di database. Ketik 1 untuk menetapkan user dengan ID 1
- Lakukan migrate dengan perintah python3 manage.py migrate
- Buka settings.py di direktori amolali_bakery, tambahkan import baru : import os
- Lalu ganti variabel DEBUG menjadi :
    PRODUCTION = os.getenv("PRODUCTION", False)
    DEBUG = not PRODUCTION

4. **Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.** :
    - Akun 1:
    ![](https://github.com/salsaaruum/amolali_bakery/blob/main/Screenshot_akun1.png)
    - Akun 2:
    ![](https://github.com/salsaaruum/amolali_bakery/blob/main/Screenshot_akun2.png)

    ada dibagian atas dan bawah
## Link Deploy PWS :
    https://salsabila-arumdapta-amolalibakery.pbp.cs.ui.ac.id


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
'image = models.URLField()', field ini untuk menambahkan gambar menggunakan link yang berasal dari internet 

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
    - Hasilnya dapat dilihat seperti pada screenshot dibawah ini merupakan hasil mencari menggunakan tampilan XML, JSON, atau menggunakan ID dalam bentuk XML ataupun JSON


## Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
- format xml :
![](https://github.com/salsaaruum/amolali_bakery/blob/main/ScreenshotXML_SalsabilaArumdapta.png)

- format json :
![](https://github.com/salsaaruum/amolali_bakery/blob/main/ScreenshotJSON_SalsabilaArumdapta.png)

- format xml dengan id :
![](https://github.com/salsaaruum/amolali_bakery/blob/main/ScreenshotXML_ID_SalsabilaArumdapta.png)

- format json dengan id :
![](https://github.com/salsaaruum/amolali_bakery/blob/main/ScreenshotJSON_ID_SalsabilaArumdapta.png)

## Link Deploy PWS :
    https://salsabila-arumdapta-amolalibakery.pbp.cs.ui.ac.id


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






