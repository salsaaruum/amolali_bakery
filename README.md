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
Method is_valid() pada form django berfungsi untuk memvalidasi input data dan memastikan bahwa data yang dimasukkan sesuai dengan aturan validasi yang ditentukan di form
- Memvalidasi input data : is_valid() untuk memeriksa apakaha data yang diinput pengguna sudah memenuhi syarat validasi yang didefinisikan pada form seperti tipe data, format email yang valid, maksimum karakter, dll
- Menandai field yang invalid : Jika terdapat data yang tidak valid maka is_valid() akan mengembalikan False dan otomatis menampilkan pesan kesalahan ke form 

Lalu mengapa kita butuh is_valid()?
- Untuk memastikan integritas data : memastikan bahwa data yang diproses atau disimpan di database sudah bersih dan valid, hal ini untuk mencegah data yang rusak atau tidak sesuai format masuk ke dalam sistem
- Keamanan aplikasi : memvalidasi data yang sangat penting untuk menghindari potensi eksploitasi seperti serangan SQL Injection atau Cross-Site Scripting (XSS), yang bisa terjadi jika input tidak divalidasi dengan baik 
- Penangan form yang sederhana : dengan is_valid(), validasi form dapat dikelola secara otomatis oleh Django, tanpa perlu memeriksa data satu per satu secara manual. Ini mempermudah penanganan form dan menjaga kode tetap bersih dan mudah dipelihara.


## 4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
Jawaban :
CSRF atau Cross-Site Request Forgery adalah jenis serangan yang memaksa pengguna untuk melakukan tindakan yang tidak diinginkan pada aplikasi web yang sudah terautentikasi. csrt_token ini berguna untuk melindungi aplikasi django dari serangan CSRF. 

Mengapa kita butuh csrf_token? 
csrf_token adalah token keamanan untuk melindungi aplikasi dari serangan CSRF. Hal ini untuk memastikan bahwa request yang dibuat oleh server benar-benar berasal dari pemiliki yang sah bukan eksternal lain yang jahat. Django secara otomatis menghasilkan token CSRF yang unik untuk tiap sesi pengguna dan memasukkannya ke form HTML. Token ini harus dikirim bersama data dorm saat pengguna mengirim request POST. Jika token valid, maka request ianggap aman. jika tidak, request akan ditolak.

Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django?
Jika form django tidak memiliki csrf_token, maka django akan **rentan terhadap serangan CSRF**. Penyerang bisa saja memanfaatkan sesi yang sudah aktif (login) untuk mengubah kata sandi, hapus akun tanpa sepengetahuan pengguna. 

Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
Penyerang bisa menggunakan teknik mengirim link berbahaya melalui email atau media sosial untuk mengarahkan korban ke halaman yang membuka akses untuk memicu permintaan otomatis ke aplikasi web yang di targetkan. Kedua, penyerang bisa membuat form tersembunyi di situs mereka yang mengirimkan permintaan POST ke aplikasi web di mana pengguna sudah terautentikasi. Penyerang juga bisa memanfaatkan gambar atau iframe yang mengarahkan ke URL tersebut dan melancarkan aksi.

Pada intinya, csrf_token berfungsi sebagai pelindung aplikasi web dari serangan CSRF yang dapat merugikan pengguna seperti kehilangan akun, password yang diganti tanpa sepengetahuan pengguna, transaksi yang tidak diingiinkan, pengubahan data dan masih banyak lagi


## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Jawaban :



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
- Selanjutnya lakukan instalasi django dan insiasi django, pada terminal yang sama jalankan perintah "python3 -m venv env"
- Kemudian aktifkan virtual environment dengan menjalankan perintah "source env/bin/active"
- Siapkan berkas requirements.txt lalu install dengan perintah "pip install -r requirements.txt", kemudian buat proyek django "django-admin startproject amolali_bakery ."
- Lakukan konfigurasi dan jalankan server dengan menambahkan string pada file settings.py "ALLOWED_HOSTS = ["localhost", "127.0.0.1"]"
- Kemudian jalankan server django dengan melakukan perintah "python3 manage.py runserver"
- Cek, jika sudah muncul animasi rocket pada http://localhost:8000, maka aplikasi django sudah berhasil dibuat
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
- Buka file "main.html" dan modifikasi dengan sintaks django untuk menampilkan nilai dari variabel yang sudah didefinisikan
- Lakukan konfigurasi routing dengan cara membuat berkas "urls.py" di dalam folder main lalu tambahkan "include" untuk menghubungkan ke tampilan main
- Jalankan lagi proyek django dengan perintah "python3 manage.py runserver" lalu cek apakah muncul animasi rocket pada "http://localhost:8000/" atau tidak
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
- Bersifat "Batteries Included" : django menyediakan fitur bawaan yang bisa digunakan tanpa memerlukan konfigurasi tambahan seperti autentikasi, pengelolaan database, pengiriman email sehingga memudahkan pemula menggunakannya dan fokus pada logika aplikasi
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
