1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Jawaban :
1. Pertama saya membuat direktori/folder di lokal berjudul "amolali_bakery"
2. Kemudian saya membuat repositori baru di Github dengan judul "amolali_bakery"
3. Selanjutnya saya melakukan konfigurasi awal git dengan memasukkan kalimat "git init" pada terminal folder lokal
4. Masukkan seluruh konfigurasi pengguna dan email, kemudian verifikasi konfigurasi 
5. Selanjutnya buat branch utama dengan perintah "git branch -M main"
6. Hubungkan folder/direktori lokal dengan repositori Github dengan perintah "git remote add origin https://github.com/salsaaruum/amolali_bakery.git"
7. Selanjutnya lakukan instalasi django dan insiasi django, pada terminal yang sama jalankan perintah "python3 -m venv env"
8. Kemudian aktifkan virtual environment dengan menjalankan perintah "source env/bin/active"
9. Siapkan berkas requirements.txt lalu install dengan perintah "pip install -r requirements.txt", kemudian buat proyek django "django-admin startproject amolali_bakery ."
10. Lakukan konfigurasi dan jalankan server dengan menambahkan string pada file settings.py "ALLOWED_HOSTS = ["localhost", "127.0.0.1"]"
11. Kemudian jalankan server django dengan melakukan perintah "python3 manage.py runserver"
12. Cek, jika sudah muncul animasi rocket pada http://localhost:8000, maka aplikasi django sudah berhasil dibuat
13. Klik ctrl + C pada keyboard untuk mematikan virtual environment
14. Buat berkas ".gitignore" untuk menentukan berkas dan direktori mana yang harus diabaikan oleh Git
15. Kemudian saya lakukan add, commit, dan push
16. Aktifkan virtual environment dengan perintah yang sama dengan sebelumnya kemudian jalankan perintah "python3 manage.py startapp main"
17. Tambahkan string "main" pada berkas settings.py "INSTALLED_APPS = ['main']"
18. Buat folder/direktori baru pada aplikasi 'main' dengan nama "templates" kemudian buat file baru dengan judul "main.html" isi sesuai kebutuhan untuk tugas ini
19. Cek apakah berkas file "main.html" dapat dibuka di peramban web dengan cara double click
20. Lalu ubah berkas models.py pada aplikasi main sesuai dengan kebutuhan dengan nama class "Product" sesuai ketentuan tugas
21. Lakukan migrasi model dengan perintah "python3 manage.py makemigrations" kemudian lakukan migrasi ke dalam basis data lokal dengan perintah "python3 manage.py migrate"
22. Buka file views.py pada aplikasi 'main' lalu tambahkan fungsi show_main dan saya sesuaikan dengan tugas saya
23. Buka file "main.html" dan modifikasi dengan sintaks django untuk menampilkan nilai dari variabel yang sudah didefinisikan
23. Lakukan konfigurasi routing dengan cara membuat berkas "urls.py" di dalam folder main lalu tambahkan "include" untuk menghubungkan ke tampilan main
24. Jalankan lagi proyek django dengan perintah "python3 manage.py runserver" lalu cek apakah muncul animasi rocket pada "http://localhost:8000/" atau tidak
25. Selamat proyek Tugas Individu 2 sudah selesai. Tidak lupa untuk melakukan add, commit, dan push untuk update isi repositori amolali_bakery pada Github 
26. Tidak lupa untuk melakukan deploy pada PWS dengan cara yang sama seperti pada Github, yaitu dengan cara membuat proyek baru dengan menu "Create New Project"
27. Masukkan nama project kemudian lakukan perintah pada project command PWS dengan mengatur remote, mengubah branch dari 'main' ke 'master' dan langkah terakhir lakukan perintah 'push pws master'
28. Klik view project maka proyek yang dibuat sudah dapat dilihat


2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
Jawaban:



3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
Jawaban:  
a. Merekam / menyimpan perubahan kode : Git memungkinkan untuk merekam atau menyimpan setiap perubahan pada kode yang disimpan dalam bentuk commit sehingga memudahkan untuk melihat siapa yang melakukan perubahan, apa, dan kapan perubahan dilakukan
b. Kolaborasi tim : Git memungkinkan beberapa pengembang kerja secara bersamaan pada proyek yang sama, terdapat fitur branching dan merging untuk kolaborasi yang lebih mudah dengan memisahkan perubahan yang sedang dikerjakan pada fitur tertentu sebelum digabung ke kode utama
c. Penyimpanan terdistribusi : Git memiliki sistem yang terdistribusi, setiap perubahan tersimpan pada riwayat proyek. Pengembang bisa bekerja secara offline dan menyinkronkan perubahan saat kembali online.
d. Mengembalikan kode ke versi sebelumnya : Jika terdapat masalah pada kode baru, pengembang dapat dengan mudah kembali ke versi kode sebelumnya. Tiap commit dapat diakses kapan saja sehingga mengurangi resiko terjadi bug atau kesalahan.
e. Integrasi dengan CI/CD: Git sering digunakan bersama dengan alat Continuous Integration/Continuous Deployment (CI/CD), seperti GitHub Actions, GitLab CI, dan lainnya, untuk otomatisasi proses pengujian, pembangunan, dan deployment setelah perubahan dikirim ke repositori.


4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Jawaban:
a. Bersifat "Batteries Included" : django menyediakan fitur bawaan yang bisa digunakan tanpa memerlukan konfigurasi tambahan seperti autentikasi, pengelolaan database, pengiriman email sehingga memudahkan pemula menggunakannya dan fokus pada logika aplikasi
b. Mengajarkan konsep pengembangan web :
-- MVT (Model View Template) : Membantu pemula memahami pemisahan antara data, logika bisnis, dan tampilan/interface
-- ORM (Object Relational Mapping) : Django menggunakan ORM untuk berinteraksi dengan datase sehingga pemula tidak perlu menulis quey SQL secara manual
-- Routing dan URL Mapping : Membantu untuk memahami dasar bagaimana URL dipetakan ke fungsi atau tampilan di aplikasi web
c. Dokumentasi yang Komprehensif: Django memiliki dokumentasi yang sangat komprehensif dan ramah pemula. Dokumentasinya memberikan banyak contoh, penjelasan, dan panduan langkah demi langkah yang memudahkan pengguna baru untuk belajar secara mandiri.
d. Terstruktur dan Scalable: Django memfasilitasi pengembangan aplikasi yang baik dan terstruktur sejak awal. Hal ini penting bagi pemula agar mereka belajar tentang pentingnya organisasi kode yang rapi, yang sangat berguna jika proyek tumbuh lebih besar dan kompleks.
e. Memiliki keamanan bawaan seperti CSRF, SQL injection, dan XSS sehingga pemula tidak perlu khawatir dengan konfigurasi yang rumit terkait keamanan


5. Mengapa model pada Django disebut sebagai ORM?
Jawaban:
Model Django disebut sebagai ORM (Object Relation Mapping) karena memungkinkan pemetaan otomatis antara objek Python dan tabel dalam database relasional. Django ORM memberikan pengembang cara yang lebih mudah dan intuitif untuk bekerja dengan database, tanpa harus berurusan langsung dengan SQL query yang kompleks, serta mendukung struktur data berorientasi objek yang lebih konsisten dengan bahasa pemrograman Python.