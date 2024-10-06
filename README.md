# Tugas 6 
## 1. Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!
Jawaban: 
- **Interaktif**: JavaScript memungkinkan pengembang untuk menambahkan elemen interaktif pada halaman web, seperti menu dropdown, modals, dan elemen yang merespons tindakan pengguna (klik, hover, dll.)
- **Pengembangan aplikasi web lebih responsif**: JavaScript memungkinkan pembuatan aplikasi web yang responsif, di mana pengguna dapat berinteraksi dengan aplikasi tanpa penundaan. Ini termasuk pembaruan konten tanpa memuat ulang halaman (melalui AJAX) dan pengambilan data dari server.
- **Manipulasi DOM**: Dengan JavaScript, pengembang dapat mengakses dan memanipulasi Document Object Model (DOM) untuk memperbarui konten dan struktur halaman web secara dinamis tanpa perlu memuat ulang halaman.
- **Pengembangan Backend**: Dengan adanya Node.js, JavaScript sekarang dapat digunakan untuk pengembangan sisi server, memungkinkan pengembang untuk menggunakan satu bahasa untuk seluruh tumpukan aplikasi (frontend dan backend).
- **Kompatibilitas Lintas Platform**: JavaScript didukung oleh semua browser modern, sehingga aplikasi yang dibangun dengan JavaScript dapat diakses di berbagai perangkat dan sistem operasi.


## 2. Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?
Jawaban:
- **Fungsi await**:
    - **Menunggu hasil**: Ketika menggunakan await dengan fetch(), JavaScript akan menunggu hingga permintaan (request) selesai dan mendapatkan respons (response) dari server sebelum melanjutkan ke baris kode berikutnya. Ini memastikan bahwa kita tidak mencoba untuk mengakses data dari respons yang belum tersedia.
    - **Menyederhanakan penanganan promise**: Dengan await, kita dapat menulis kode yang lebih bersih dan lebih mudah dibaca, mirip dengan penulisan kode sinkron. Tanpa await, kita akan memerlukan chaining .then() yang dapat membuat kode menjadi lebih rumit.

- **Apa yang terjadi jika tidak menggunakan await**:
    - **Promise tidak teratasi**: jika tidak menggunakan await, fetch() akan tetap mengembalikan promise, dan eksekusi kode akan terus berlanjut tanpa menunggu respons. Ini bisa menyebabkan kita mencoba mengakses data sebelum data tersebut tersedia.
    - **Kesalahaan dalam penanganan respons**: Tanpa await, kita tidak akan bisa mendapatkan data dari respons secara langsung. Hal ini akan menyebabkan kita memerlukan cara lain untuk menangani promise, seperti menggunakan .then().
    - **Potensi adanya bug**: Tidak menggunakan await bisa menyebabkan bug yang sulit ditemukan karena kode yang bergantung pada data dari server akan dieksekusi sebelum data tersebut tersedia.


## 3. Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?
Jawaban:
- **Perlindungan CSRF**: Django secara otomatis akan mengaktifkan perlindungan CSRF untuk semua view yang menggunakan metode POST. Hal ini bertujuan untuk mencegah serangan pihak ketiga untuk mengirim permintaan tidak sah atas nama pengguna tanpa sepengetahuan mereka. Dengan CSRF, setiap formulir yang dikirimkan harus menyertakan token CSRF yang valid.
- **Permintaan AJAX dann token CSRF**: Ketika kita mengirimkan permintaan AJAX dengan metode POST, kita perlu memastikan bahwa token CSRF dikirim bersama dengan permintaan tersebut. Jika tidak, Django akan menolak permintaan tersebut dan mengembalikan kesalahan 403 (Forbidden). Jika kita tidak ingin menangani pengiriman token CSRF secara manual untuk setiap permintaan AJAX, kita dapat menggunakan csrf_exempt.
- **Penggunaan csrf_exempt**: Dengan menggunakan csrf_exempt, kita memberi tahu Django untuk tidak menerapkan pemeriksaan CSRF pada view tertentu. Ini sangat berguna dalam situasi berikut:
    - API Endpoints
    - Simplicity
- **Risiko keamanan**: Meskipun csrf_exempt membuat pengembangan lebih mudah, penggunaannya harus dilakukan dengan hati-hati. Menonaktifkan perlindungan CSRF dapat membuka aplikasi kita terhadap serangan yang berpotensi merugikan. Sebaiknya, hanya gunakan csrf_exempt pada view yang benar-benar membutuhkan pengecualian ini, dan pastikan untuk melakukan validasi yang ketat pada data yang diterima.


## 4. Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?
Jawaban:
- **Keamanan**: 
    - **Menghindari Manipulasi oleh Pengguna**: Validasi di frontend bisa diabaikan atau dimanipulasi oleh pengguna yang paham teknologi, misalnya dengan menggunakan alat seperti browser developer tools atau aplikasi pihak ketiga. Oleh karena itu, backend harus tetap memeriksa dan membersihkan data untuk mencegah input berbahaya atau tidak valid.
    - **Mencegah Serangan Berbasis Input**: Serangan seperti SQL Injection atau Cross-Site Scripting (XSS) sering kali memanfaatkan data input yang tidak divalidasi dengan baik. Backend memiliki kontrol penuh terhadap validasi ini dan dapat melindungi sistem dari serangan tersebut.

- **Integritas data**:
    - **Frontend Dapat Dilewati**: Validasi frontend tergantung pada kode JavaScript yang berjalan di browser pengguna. Karena kode ini bisa dimodifikasi atau bahkan dihilangkan, server harus memastikan bahwa data yang masuk sudah aman dan sesuai standar.
    - **Keandalan Validasi**: Pada sisi frontend, validasi dan pembersihan dapat dilakukan untuk meningkatkan pengalaman pengguna (user experience) dengan memberikan umpan balik yang cepat. Namun, karena data pada akhirnya akan diproses oleh server, validasi dan pembersihan di backend memastikan bahwa data yang disimpan dalam sistem selalu memenuhi persyaratan.

- **Mengatasi lingkungan yang berbeda**:
    - **Mengatasi Masalah Browser dan Perangkat**: Tidak semua pengguna memiliki browser yang mendukung validasi yang diterapkan di frontend. Backend, di sisi lain, selalu memiliki kontrol penuh atas validasi yang diperlukan dan bekerja secara konsisten di semua perangkat dan browser.


## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
Jawaban:
**AJAX GET**
 - **Ubahlah kode cards data mood agar dapat mendukung AJAX GET**:
    1. Tambahkan import pada file 'views.py':
        from django.views.decorators.csrf import csrf_exempt
        from django.views.decorators.http import require_POST
    2. Buat parameter baru pada file 'views.py' untuk menerima request:
        @csrf_exempt
        @require_POST
        def add_product_entry_ajax(request):
            name = strip_tags(request.POST.get("name")) #strip HTML tags!
            price = request.POST.get("price")
            description = strip_tags(request.POST.get("description")) #strip HTML tags!
            category = request.POST.get("category")
            image = request.POST.get("image")
            user = request.user

            new_product = Product(
                name=name, 
                price=price,
                description=description,
                category=category,
                image=image,
                user=user
            )
            new_product.save()

            return HttpResponse(b"CREATED", status=201)

 - **Lakukan pengambilan data mood menggunakan AJAX GET. Pastikan bahwa data yang diambil hanyalah data milik pengguna yang logged-in**: 
    3. Untuk menampilkan Data product entry dengan fetch() API, buka file 'views.py' lalu hapus baris :
        product_entries = Product.objects.filter(user=request.user) dan 
        'product_entries': product_entries,
    4. Buka file 'views.py', ubah baris pertama views untuk show_xml dan show_json:
        data = Product.objects.filter(user=request.user)
    5. Buka file 'main.html' lalu hapus block conditional product_entries untuk menampilkan card_product kosong atau tidak:
        {% if not product_entries %}
            <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
                <img src="{% static 'image/sedih-banget.png' %}" alt="Sad face" class="w-32 h-32 mb-4"/>
                <p class="text-center text-gray-600 mt-4">Belum ada barang yang dijual nih...</p>
            </div>
            {% else %}
            <div class="columns-1 sm:columns-2 lg:columns-3 gap-6 space-y-6 w-full">
                {% for product in product_entries %}
                    {% include 'card_product.html' with product=product %}
                {% endfor %}
            </div>
            {% endif %}
    6. Tambahkan potongan kode ini:
        ...
        <div id="product_entry_cards"></div>
        ...
    7. Buatlah block <script/> dibagian bawah berkas sebelum endblock content dan buatlah fungsi dengan nama getProductEntries:
        async function getProductEntries(){
            return fetch("{% url 'main:show_json' %}").then((res) => res.json())
        }

**AJAX POST**
 - **Buatlah sebuah tombol yang membuka sebuah modal dengan form untuk menambahkan mood**:
    1. Tambahkan kode untuk implementasi modal (tailwind), main/templates/main.html:
        <div id="crudModal" tabindex="-1" aria-hidden="true" class="hidden fixed inset-0 z-50 w-full flex items-center justify-center bg-gray-800 bg-opacity-50 overflow-x-hidden overflow-y-auto transition-opacity duration-300 ease-out">
        <div id="crudModalContent" class="relative bg-white rounded-lg shadow-lg w-5/6 sm:w-3/4 md:w-1/2 lg:w-1/3 mx-4 sm:mx-0 transform scale-95 opacity-0 transition-transform transition-opacity duration-300 ease-out">
        <!-- Modal header -->
        <div class="flex items-center justify-between p-4 border-b rounded-t">
        <h3 class="text-xl font-semibold text-gray-900">
        Add New Product
    </h3>
    <button type="button" class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center" id="closeModalBtn">
    <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
    <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path>
    </svg>
    <span class="sr-only">Close modal</span>
    </button>
    </div>

    <!-- Modal body -->
    <div class="px-6 py-4 space-y-6 form-style">
    <form id="ProductForm">
        
    <!-- Product Name -->
    <div class="mb-4">
    <label for="name" class="block text-sm font-medium text-gray-700">Product Name</label>
    <input type="text" id="name" name="name" class="mt-1 block w-full border border-gray-300 rounded-md p-2 hover:border-indigo-700" placeholder="Enter product name" required>
    </div>

    <!-- Price -->
    <div class="mb-4">
    <label for="price" class="block text-sm font-medium text-gray-700">Price</label>
    <input type="number" id="price" name="price" class="mt-1 block w-full border border-gray-300 rounded-md p-2 hover:border-indigo-700" placeholder="Enter price" required>
    </div>

    <!-- Description -->
    <div class="mb-4">
    <label for="description" class="block text-sm font-medium text-gray-700">Description</label>
    <textarea id="description" name="description" rows="3" class="mt-1 block w-full h-52 resize-none border border-gray-300 rounded-md p-2 hover:border-indigo-700" placeholder="Enter product description" required></textarea>
    </div>

    <!-- Category -->
    <div class="mb-4">
    <label for="category" class="block text-sm font-medium text-gray-700">Category</label>
    <input type="text" id="category" name="category" class="mt-1 block w-full border border-gray-300 rounded-md p-2 hover:border-indigo-700" placeholder="Enter product category">
    </div>

    <!-- Image URL -->
    <div class="mb-4">
    <label for="image" class="block text-sm font-medium text-gray-700">Image URL</label>
    <input type="url" id="image" name="image" class="mt-1 block w-full border border-gray-300 rounded-md p-2 hover:border-indigo-700" placeholder="Enter image URL" required>
    </div>
    </form>
    </div>

    <!-- Modal footer -->
    <div class="flex flex-col space-y-2 md:flex-row md:space-y-0 md:space-x-2 p-6 border-t border-gray-200 rounded-b justify-center md:justify-end">
    <button type="button" class="bg-gray-500 hover:bg-gray-600 text-white font-bold py-2 px-4 rounded-lg" id="cancelButton">Cancel</button>
    <button type="submit" id="submitProductEntry" form="ProductForm" class="bg-indigo-700 hover:bg-indigo-600 text-white font-bold py-2 px-4 rounded-lg">Save</button>
    </div>
    </div>
    </div>

    2. Tambahkan fungsi-fungsi JavScript agar modal dapat berfungsi:
        <script>
            ...
        const modal = document.getElementById('crudModal');
        const modalContent = document.getElementById('crudModalContent');

        function showModal() {
            const modal = document.getElementById('crudModal');
            const modalContent = document.getElementById('crudModalContent');

            modal.classList.remove('hidden'); 
            setTimeout(() => {
                modalContent.classList.remove('opacity-0', 'scale-95');
                modalContent.classList.add('opacity-100', 'scale-100');
            }, 50); 
        }

        function hideModal() {
            const modal = document.getElementById('crudModal');
            const modalContent = document.getElementById('crudModalContent');

            modalContent.classList.remove('opacity-100', 'scale-100');
            modalContent.classList.add('opacity-0', 'scale-95');

            setTimeout(() => {
                modal.classList.add('hidden');
            }, 150); 
        }

        document.getElementById("cancelButton").addEventListener("click", hideModal);
        document.getElementById("closeModalBtn").addEventListener("click", hideModal);
                </script>

    3. Ubah bagian tombol Add New Product yang sudah ditambahkan di tugas sebelumnya dan tambah tombol baru untuk menambahkan data dengan AJAX:
        ...
            <a href="{% url 'main:create_product' %}" class="bg-indigo-400 hover:bg-indigo-400 text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105 mx-4 ">
            Add New Product
            </a>
            <button data-modal-target="crudModal" data-modal-toggle="crudModal" class="btn bg-indigo-700 hover:bg-indigo-600 text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105" onclick="showModal();">
            Add New Product by AJAX
            </button>
        ...

 - **Buatlah fungsi view baru untuk menambahkan mood baru ke dalam basis data**:
    4. def add_product_entry_ajax(request):
            name = strip_tags(request.POST.get("name")) #strip HTML tags!
            price = request.POST.get("price")
            description = strip_tags(request.POST.get("description")) #strip HTML tags!
            category = request.POST.get("category")
            image = request.POST.get("image")
            user = request.user

            new_product = Product(
                name=name, 
                price=price,
                description=description,
                category=category,
                image=image,
                user=user
            )
            new_product.save()

            return HttpResponse(b"CREATED", status=201)

 - **Buatlah path /create-ajax/ yang mengarah ke fungsi view yang baru kamu buat**:
    5.         urlpatterns = [
                    ...
                    path('create-product-entry-ajax', add_product_entry_ajax, name='add_product_entry_ajax'),
                ]

 - **Hubungkan form yang telah kamu buat di dalam modal kamu ke path /create-ajax/**:

    6. Tambahkan routing untuk fungsi add_product_entry_ajax, buka 'urls.py', tambahkan import dan path url:
        from main.views import ..., add_mood_entry_ajax

        urlpatterns = [
            ...
            path('create-product-entry-ajax', add_product_entry_ajax, name='add_product_entry_ajax'),
        ]

 - **Lakukan refresh pada halaman utama secara asinkronus untuk menampilkan daftar mood terbaru tanpa reload halaman utama secara keseluruhan**:
    7.     9. Buat fungsi baru block <script/> dengan nama refreshProductEntries untuk me-refresh data product secara asinkronus:
          async function refreshProductEntries() {
            document.getElementById("product_entry_cards").innerHTML = "";
            document.getElementById("product_entry_cards").className = "";
            const productEntries = await getProductEntries();
            let htmlString = "";
            let classNameString = "";

            if (productEntries.length === 0) {
                classNameString = "flex flex-col items-center justify-center min-h-[24rem] p-6";
                htmlString = `
                    <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
                        <img src="{% static 'image/sedih-banget.png' %}" alt="Sad face" class="w-32 h-32 mb-4"/>
                        <p class="text-center text-gray-600 mt-4">Belum ada data product pada Amolali Bakery</p>
                    </div>
                `;
            }
            else {
                classNameString = "columns-1 sm:columns-2 lg:columns-3 gap-6 space-y-6 w-full"
                productEntries.forEach((item) => {
                    htmlString += `
                    <div class="relative break-inside-avoid">
                        <div class="relative top-5 bg-indigo-100 shadow-md rounded-lg mb-6 break-inside-avoid flex flex-col border-2 border-indigo-300 transform rotate-1 hover:rotate-0 transition-transform duration-300">
                            <div class="bg-indigo-200 text-gray-800 p-4 rounded-t-lg border-b-2 border-indigo-300">
                                <h3 class="font-bold text-xl mb-2">${name}</h3>
                                <p class="text-gray-600">Price: ${item.fields.price}</p>
                            </div>
                            <div class="p-4">
                                <p class="font-semibold text-lg mb-2">Description</p>
                                <p class="text-gray-700 mb-2">${description}</p>
                                <img src="${item.fields.image}" alt="${item.fields.name}" class="w-full h-auto rounded-lg mt-4">
                            </div>
                        </div>
                        <div class="absolute top-0 -right-4 flex space-x-1">
                            <a href="/edit-product/${item.pk}" class="bg-yellow-500 hover:bg-yellow-600 text-white rounded-full p-2 transition duration-300 shadow-md">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">
                                    <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
                                </svg>
                            </a>
                            <a href="/delete/${item.pk}" class="bg-red-500 hover:bg-red-600 text-white rounded-full p-2 transition duration-300 shadow-md">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">
                                    <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
                                </svg>
                            </a>
                        </div>
                    </div>
                    `;
                });
            }
            document.getElementById("product_entry_cards").className = classNameString;
            document.getElementById("product_entry_cards").innerHTML = htmlString;
        }
        refreshProductEntries();
        




# Tugas 5
## 1.  Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Jawaban:
Terdapat beberapa selector yang berlaku di CSS untuk satu elemen HTML, urutan prioritasnya menentukan gaya mana yang diterapkan. Urutan prioritasnya antara lain :
- **Inline Styles** : Gaya yang didefinisikan langsung pada elemen dengan atribut style="" memiliki prioritas tertinggi. Selektor ini memiliki specificity tertinggi. Contoh:
    <p style="color: red;">Text</p>
- **ID Selectors** : Selektor yang menggunakan ID elemen. Selektor ini memiliki tingkat specificity yang lebih tinggi daripada class, pseudo-class, atau element selector. Contoh:
        #header {
        color: blue;
    }
- **Class Selectors, Attribute Selectors, Pseudo-Class Selectors** : Selektor ini menggunakan class, atribut, aatu pseudo-class. Contoh: 
        .menu {
        color: green;
    }
    [type="text"] {
        border: 1px solid black;
    }
    :hover {
        color: yellow;
    }
- **Element selectors dan pseudo-element selectors** : Selektor yang menggunakan elemen HTML langsung atau pseudo-element seperti ::before dan ::after. Contoh:
        p {
            color: black;
        }
- **Universal selector(*) dan inheritance** : Universal selector dan gaya yang dihasilkan melalui pewarisan dari elemen parent memiliki prioritas paling rendah.
- **!important** : Deklarasi dengan !important akan mengesampingkan semua prioritas selector lainnya, terlepas dari specificity.
    .content {
        color: green !important;
    }
Jika digunakan, maka teks akan berwarna hijau, walaupun ada ID atau inline style



## 2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
Jawaban: 
Responsive design menjadi konsep yang penting dalam pengembangan aplikasi web karena :
- **Meningkatkan pengalaman pengguna (UX)**: Aplikasi web yang lebih responsive akan memudahkan pelanggan dalam menggunakannya. Hal ini karena elemen-elemen seperti tombol, teks, gambarnya menyesuaikan layar. Hal ini menghindari masalah yang dapat ditimbulkan seperti teks yang terlalu kecil, gambar yang tidak proposional, tombol yang tidak bisa ditekan, dan masih banyak lagi. Sehingga, pengguna nyaman dalam menggunakan aplikasi web tersebut
- **Dapat digunakan di beragam perangkat**: Pengguna bisa mengakses aplikasi web melalui berbagai perangkat seperti smartphone, tablet, laptop, dekstop dengan layar dan resolusi yang berbeda. Hal ini terjadi karena responsive design memastikan tampilan aplikasi web secara otomatis menyesuaikan tampilan sesuai perangkat tanpa harus mengembangkan versi terpisah untuk tiap jenis perangkat. Tentunya hal ini menghemat biaya dan waktu sehingga lebih efisien dalam pemeliharaan aplikasi
- **Optimisasi performa**: Dengan responsive deisgn, elemen yang terdapat pada aplikasi web seperti gambar, tombol, teks, dan fitur-fitur lainnya dapat dioptimalkan dengan perangkat dengan layar yang kecil maupun yang besar. Hal ini membantu meningkatkan kecepatan dan efisiensi loading halaman terutama di perangkat dengan keterbatasan bandwidth

**Contoh aplikasi yang sudah menerapkan responsive design** :
- **YouTube**:
YouTube menyesuaikan tampilannya untuk berbagai perangkat dengan cara mengubah tata letak video, navigasi, dan thumbnail agar sesuai dengan ukuran layar pengguna. Pada perangkat mobile, video akan menyesuaikan secara otomatis dengan ukuran layar, dan menu navigasi akan menjadi lebih kompak.
- **Spotify**:
Platform streaming musik ini menggunakan responsive design untuk memberikan pengalaman yang konsisten di semua perangkat. Pada desktop, playlist dan kontrol musik tersedia dalam sidebar. Di perangkat mobile, elemen-elemen seperti tombol play, pause, dan playlist disesuaikan untuk ukuran layar yang lebih kecil dengan navigasi swipe dan menu yang lebih ringkas.
- **Netflix**:
Aplikasi streaming film ini menampilkan desain responsif untuk mendukung pengalaman menonton dari perangkat apa pun.
Di desktop, pengguna dapat melihat banyak pilihan kategori film dalam satu tampilan grid. Sementara di mobile, konten disusun vertikal dengan navigasi swipe, dan elemen seperti kontrol pemutaran mudah diakses.

**Contoh aplikasi yang belum menerapkan responsive design** :
- **Situs Web Perusahaan Lama**:
Banyak perusahaan tradisional dengan situs web lama yang belum dioptimalkan untuk perangkat mobile atau tablet. Desainnya biasanya kaku dan tidak berubah sesuai ukuran layar. Situs perusahaan manufaktur atau layanan lokal yang masih menggunakan layout statis, di mana elemen-elemen tidak menyesuaikan dengan baik ketika diakses dari perangkat mobile.
- **Situs Web Pemerintah Tua**:
Banyak situs web pemerintah, terutama yang dibuat beberapa tahun lalu, tidak dioptimalkan untuk pengalaman mobile. Pengguna sering kali harus memperbesar dan menggulir secara horizontal untuk membaca konten. Situs layanan pemerintah lokal yang menampilkan informasi berbasis tabel besar, form pendaftaran, atau data statistik yang hanya terlihat baik di layar desktop, tetapi sulit digunakan di smartphone.



## 3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
Jawaban: 
- **Margin** : 
    - **Pengertian** : Margin adalah ruang kosong di luar elemen. Margin digunakan untuk menentukan jarak antar elemen dengan elemen lainnya di halaman web. Hal ini memungkinkan elemen memiliki "napas" dan tidak terasa padat atau bertumpuk. Selain itu, margin digunakan untuk menghindari overlap, menciptakan estetika dan desain, menciptakan aplikasi yang responsiv dan untuk mengontrol layout
    - **Cara Implementasi** : 
        1. Tentukan elemen yang ingin diberi margin
        2. Tambahkan properti margin ke dalam CSS, contoh:
            h1 {
                margin: 20px 10px;
            }
        3. Gunakan properti margin spesifik jika diperlukan
        4. Eksperimen dengan value negatif
        5. Uji tampilan di browser

- **Border** :
    - **Pengertian** : Border adalah garis di sekitra elemen. Border membungkus elemen dan padding, memberikan garis pembatas yang mengelilingi konten elemen tersebut. Border bisa diatur dengan ketebalan, warna, dan gaya (solid, dashed, dotted)
    - **Cara Implementasi** :
        1. Pilih elemen yang ingin diberi border
        2. Tambahkan properti border ke dalam CSS, contoh:
            h1 {
                border: 2px solid black;
            }
        3. Gunakan properti border spesifik jika diperlukan
        4. Eksperimen border dengan berbagai gaya border, contoh:
            .box {
                border: 4px groove gray;   /* Border dengan efek 3D */
            }

        5. Uji tampilannya di browser

- **Padding** :
    - **Pengertian** : Padding adalah ruang kosong di dalam elemen, yaitu jarak antara konten elemen (misalnya teks atau gambar) dengan tepi dalam border elemen. Jarak dalam padding memastikan teks tidak terlalu dekat dengan tepi, membuatnya lebih mudah dibaca. 
    - **Cara Implementasi** :
        1. Tentukan elemen yang ingin diberi padding
        2. Buka berkas CSS
        3. Tuliskan selector untuk elemen tersebut
        4. Tentukan properti padding yang ingin digunakan
        5. Simpan dan muat ulang halaman web
        contoh:
        elemen HTML:
        <div class="kotak">Ini adalah konten di dalam kotak</div>
        tambahkan padding:
        .kotak {
            border: 2px solid black; 
            padding: 20px;
        }



## 4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
Jawaban:
- **Flex Box** :
    - **Konsep** :
        1. Flexbox adalah model tata letak satu dimensi yang memudahkan pengaturan elemen di sepanjang satu sumbu, baik horizontal (baris) maupun vertikal (kolom). Flexbox sangat berguna ketika kita ingin mengatur tata letak dalam baris atau kolom secara fleksibel dan dinamis.
        2. Flexbox mendukung penyusunan elemen secara responsif, memungkinkan elemen untuk mengisi ruang yang tersedia atau menyesuaikan ukuran mereka secara otomatis berdasarkan kebutuhan.

    - **Kegunaan** :
        1. **Mengontrol perataan elemen**: Dengan Flexbox, kita bisa mengatur perataan elemen secara vertikal atau horizontal dengan mudah tanpa menggunakan banyak properti lainnya.
        2. **Mengatur elemen dalam satu baris atau kolom**: Flexbox memungkinkan kita untuk mengatur elemen menjadi baris atau kolom dan menyesuaikan distribusi ruang antar elemen.
        3. **Mendistribusikan ruang kosong**: Elemen dalam Flexbox dapat secara otomatis diperluas atau diperkecil untuk memanfaatkan ruang yang tersedia secara optimal.

- **Grid Layout** :
    - **Konsep** :
        1. Grid Layout adalah model tata letak dua dimensi yang lebih canggih dan fleksibel dibandingkan Flexbox. Grid memungkinkan kita untuk membuat tata letak baris dan kolom secara bersamaan, memberikan kontrol yang lebih baik untuk elemen-elemen pada grid yang kompleks.
        2. Grid memungkinkan kita untuk membuat tata letak yang sangat presisi, di mana elemen-elemen bisa diatur dalam sebuah grid dengan ukuran kolom dan baris yang ditentukan.

    - **Kegunaan** :
        1. **Mengontrol posisi elemen secara presisi**: Kita bisa menempatkan elemen pada grid di lokasi tertentu dengan mengatur nomor baris dan kolom.
        2. **Responsivitas yang lebih**: Dengan Grid, kita bisa membuat tata letak yang berubah sesuai ukuran layar, termasuk mengatur berapa banyak kolom atau baris yang muncul di layar yang lebih kecil.
        3. **Menyusun tata letak dua dimensi**: Grid sangat berguna untuk membangun tata letak kompleks dengan baris dan kolom yang banyak, seperti tata letak halaman majalah, dashboard, atau galeri gambar.



## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
Jawaban: 
- **Implementasikan fungsi untuk menghapus dan mengedit product** 
    1. Buat fungsi untuk mengedit product dengan parameter request dan id di 'views.py' di direktori main :
    def edit_product(request, id):
        # Get product berdasarkan id
        product = Product.objects.get(pk = id)

        # Set product sebagai instance dari form
        form = ProductForm(request.POST or None, instance=product)

        if form.is_valid() and request.method == "POST":
            # Simpan form dan kembali ke halaman awal
            form.save()
            return HttpResponseRedirect(reverse('main:show_main'))

        context = {'form': form}
        return render(request, "edit_product.html", context)
    2. Tambahkan import di file 'views.py':
        from django.shortcuts import .., reverse
        from django.http import .., HttpResponseRedirect
    3. Buat file HTML dengan judul 'edit_product.html' di direktori main/templates :
        {% extends 'base.html' %}

        {% load static %}

        {% block content %}

        <h1>Edit Mood</h1>

        <form method="POST">
            {% csrf_token %}
            <table>
                {{ form.as_table }}
                <tr>
                    <td></td>
                    <td>
                        <input type="submit" value="Edit Mood"/>
                    </td>
                </tr>
            </table>
        </form>

        {% endblock %}
    4. Buka 'urls.py', import fungsi edit_product, kemudian tambahkan path url nya kedalam urlpatterns
            from main.views import edit_product

            path('edit-product/<uuid:id>', edit_product, name='edit_product'),
    5. Buka file main.html, tambahkan kode agar ada tombol edit di setiap produk yang sudah ada 
        ...
        <tr>
            ...
            <td>
                <a href="{% url 'main:edit_product' product.pk %}">
                    <button>
                        Edit
                    </button>
                </a>
            </td>
        </tr>
        ...
    6. Lakukan hal yang sama untuk membuat fungsi menghapus produk. Buka file 'views.py' lalu buat fungsi berjudul delete_product
        def delete_product(request, id):
            # Get product berdasarkan id
            product = Product.objects.get(pk = id)
            # Hapus product
            product.delete()
            # Kembali ke halaman awal
            return HttpResponseRedirect(reverse('main:show_main'))
    7. Buka 'urls.py' import fungsi tadi dan tambahkan path url nya ke dalam urlpatterns
        from main.views import delete_product

        ...
        path('delete/<uuid:id>', delete_product, name='delete_product'), 
        ...
    8. Buka file main.html, tambahkan kode agar ada tombol edit di setiap produk yang sudah ada, 
        ...
        <tr>
            ...
            <td>
                <a href="{% url 'main:edit_product' product.pk %}">
                    <button>
                        Edit
                    </button>
                </a>
            </td>
            <td>
                <a href="{% url 'main:delete_product' product.pk %}">
                    <button>
                        Delete
                    </button>
                </a>
            </td>
        </tr>
        ...
    
- **Kustomisasi halaman login, register, dan tambah product semenarik mungkin**
    1. Halaman login :
        - Buat file berjudul login.html
        - Modifikasi agar tampilan terdapat tombol login, bila belum punya akun pengguna dapat melakukan registrasi terlebih dahulu
        - Saya memilih tema berwarna pink :
        {% extends 'base.html' %}

        {% block meta %}
        <title>Login</title>
        {% endblock meta %}

        {% block content %}
        <div class="min-h-screen flex items-center justify-center w-screen bg-gray-100 py-12 px-4 sm:px-6 lg:px-8">
        <div class="max-w-md w-full space-y-8">
            <div>
            <h2 class="mt-6 text-center text-black text-3xl font-extrabold text-gray-900">
                Login to your account
            </h2>
            </div>
            <form class="mt-8 space-y-6" method="POST" action="">
            {% csrf_token %}
            <input type="hidden" name="remember" value="true">
            <div class="rounded-md shadow-sm -space-y-px">
                <div>
                <label for="username" class="sr-only">Username</label>
                <input id="username" name="username" type="text" required class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-pink-500 focus:border-pink-500 focus:z-10 sm:text-sm" placeholder="Username">
                </div>
                <div>
                <label for="password" class="sr-only">Password</label>
                <input id="password" name="password" type="password" required class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-pink-500 focus:border-pink-500 focus:z-10 sm:text-sm" placeholder="Password">
                </div>
            </div>

            <div>
                <!-- Tombol login warna pink -->
                <button type="submit" class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-pink-500 hover:bg-pink-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-pink-500">
                Sign in
                </button>
            </div>
            </form>

            {% if messages %}
            <div class="mt-4">
            {% for message in messages %}
            {% if message.tags == "success" %}
                    <div class="bg-green-100 border border-green-400 text-green-700 px-4 py-3 rounded relative" role="alert">
                        <span class="block sm:inline">{{ message }}</span>
                    </div>
                {% elif message.tags == "error" %}
                    <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
                        <span class="block sm:inline">{{ message }}</span>
                    </div>
                {% else %}
                    <div class="bg-blue-100 border border-blue-400 text-blue-700 px-4 py-3 rounded relative" role="alert">
                        <span class="block sm:inline">{{ message }}</span>
                    </div>
                {% endif %}
            {% endfor %}
            </div>
            {% endif %}

            <div class="text-center mt-4">
            <p class="text-sm text-black">
                Don't have an account yet?
                <!-- Tombol register warna pink -->
                <a href="{% url 'main:register' %}" class="font-medium text-pink-500 hover:text-pink-600">
                Register Now
                </a>
            </p>
            </div>
        </div>
        </div>
        {% endblock content %}
    
    2. Halaman registrasi :
        - Buat file berjudul register.html
        - Modifikasi agar tampilan menu untuk membuat username, membnuat password, dan verifikasi password
        - Saya memilih tema berwarna pink :
        {% extends 'base.html' %}

        {% block meta %}
        <title>Register</title>
        {% endblock meta %}

        {% block content %}
        <div class="min-h-screen flex items-center justify-center bg-gray-100 py-12 px-4 sm:px-6 lg:px-8">
        <div class="max-w-md w-full space-y-8 form-style">
            <div>
            <h2 class="mt-6 text-center text-3xl font-extrabold text-black">
                Create your account
            </h2>
            </div>
            <form class="mt-8 space-y-6" method="POST">
            {% csrf_token %}
            <input type="hidden" name="remember" value="true">
            <div class="rounded-md shadow-sm -space-y-px">
                {% for field in form %}
                <div class="{% if not forloop.first %}mt-4{% endif %}">
                    <label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-black">
                    {{ field.label }}
                    </label>
                    <div class="relative">
                    {{ field }}
                    <div class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
                        {% if field.errors %}
                        <svg class="h-5 w-5 text-red-500" fill="currentColor" viewBox="0 0 20 20">
                            <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd" />
                        </svg>
                        {% endif %}
                    </div>
                    </div>
                    {% if field.errors %}
                    {% for error in field.errors %}
                        <p class="mt-1 text-sm text-red-600">{{ error }}</p>
                    {% endfor %}
                    {% endif %}
                </div>
                {% endfor %}
            </div>

            <div>
                <!-- Tombol register warna pink -->
                <button type="submit" class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-pink-500 hover:bg-pink-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-pink-500">
                Register
                </button>
            </div>
            </form>

            {% if messages %}
            <div class="mt-4">
            {% for message in messages %}
            <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
                <span class="block sm:inline">{{ message }}</span>
            </div>
            {% endfor %}
            </div>
            {% endif %}

            <div class="text-center mt-4">
            <p class="text-sm text-black">
                Already have an account?
                <!-- Link login menggunakan warna pink -->
                <a href="{% url 'main:login' %}" class="font-medium text-pink-200 hover:text-pink-300">
                Login here
                </a>
            </p>
            </div>
        </div>
        </div>
        {% endblock content %}
    
    3. Product yang saya buat sudah cukup banyak dan tiap product sudah memiliki foto untuk gambaran produknya

- **Jika pada aplikasi belum ada product yang tersimpan, halaman daftar product akan menampilkan gambar dan pesan bahwa belum ada product yang terdaftar** 
    1. Download gambar sedih kemudian simpan dengan nama apapun, saya simpan dengan nama 'sedih-banget.png'
    2. Simpan gambar di dalam folder static lalu buat folder baru dengan nama image. static/image/
    3. Simpan ke dalam template main.html yang sudah disesuaikan dengan card_info.html untuk info data pengguna dan card_product untuk rincian deskripsi product beserta field-field lain. 
        {% extends 'base.html' %}
        {% load static %}

        {% block meta %}
        <title>Amolali Bakery</title>
        {% endblock meta %}
        {% block content %}
        {% include 'navbar.html' %}
        <div class="overflow-x-hidden px-4 md:px-8 pb-8 pt-24 min-h-screen bg-gray-100 flex flex-col">
        <div class="p-2 mb-6 relative">
            <div class="relative grid grid-cols-1 z-30 md:grid-cols-3 gap-8">
            {% include "card_info.html" with title='NPM' value=npm %}
            {% include "card_info.html" with title='Name' value=name %}
            {% include "card_info.html" with title='Class' value=class %}
            </div>
        </div>
            <div class="px-3 mb-4">
            <div class="flex rounded-md items-center bg-pink-600 py-2 px-4 w-fit">
                <h1 class="text-white text-center">Last Login: {{last_login}}</h1>
            </div>
            </div>
            <div class="flex justify-end mb-6">
                <a href="{% url 'main:create_product' %}" class="bg-pink-600 hover:bg-pink-700 text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105">
                    Add New Product
                </a>
            </div>
            
            {% if not product_entries %}
            <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
                <img src="{% static 'image/sedih-banget.png' %}" alt="Sad face" class="w-32 h-32 mb-4"/>
                <p class="text-center text-gray-600 mt-4">Belum ada barang yang dijual nih...</p>
            </div>
            {% else %}
            <div class="columns-1 sm:columns-2 lg:columns-3 gap-6 space-y-6 w-full">
                {% for product in product_entries %}
                    {% include 'card_product.html' with product=product %}
                {% endfor %}
            </div>
            {% endif %}
        </div>
        {% endblock content %}

- **Jika sudah ada product yang tersimpan, halaman daftar product akan menampilkan detail setiap product dengan menggunakan card (tidak boleh sama persis dengan desain pada Tutorial!)**
    1. Bagian ini diatur dalam card_product.html. 
    2. Saya membuat dengan tema yang sama yaitu berwarna pink 
    3. Terdapat nama, harga, deskripsi, kategori, serta gambar produk di dalam setiap 1 kartu produk 
        <div class="relative break-inside-avoid">
            <div class="absolute top-2 z-10 left-1/2 -translate-x-1/2 flex items-center -space-x-2">
                <div class="w-[3rem] h-8 bg-pink-400 rounded-md opacity-80 -rotate-90"></div>
            </div>
            <div class="relative top-5 bg-pink-100 shadow-md rounded-lg mb-6 break-inside-avoid flex flex-col border-2 border-pink-300 transform rotate-1 hover:rotate-0 transition-transform duration-500">
                <div class="bg-pink-200 text-gray-800 p-4 rounded-t-lg border-b-2 border-pink-300">
                    <h3 class="font-bold text-xl mb-2">{{ product.name }}</h3>
                    <p class="text-pink-900">Price: Rp {{ product.price }}</p>
                </div>
                <div class="p-4">
                    <p class="font-semibold text-lg mb-2">Description</p>
                    <p class="text-gray-700 mb-2">{{ product.description }}</p>
                    <p class="font-semibold text-lg mb-2">Category: {{ product.category }}</p>
                    <img src="{{ product.image }}" alt="{{ product.name }}" class="rounded-lg mt-2">
                </div>
            </div>
            <div class="absolute top-0 -right-4 flex space-x-1">
                <a href="{% url 'main:edit_product' product.id %}" class="bg-purple-500 hover:bg-purple-700 text-white rounded-full p-2 transition duration-300 shadow-md">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">
                        <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
                    </svg>
                </a>
                <a href="{% url 'main:delete_product' product.id %}" class="bg-aqua-500 hover:bg-aqua-600 text-black rounded-full p-2 transition duration-300 shadow-md">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">
                        <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
                    </svg>
                </a>
            </div>
            </div>

- **Untuk setiap card product, buatlah dua buah button untuk mengedit dan menghapus product pada card tersebut!**
    1. Bagian ini diatur dalam 'card_product.html'
    2. Berikut kode nya :
          <div class="absolute top-0 -right-4 flex space-x-1">
            <a href="{% url 'main:edit_product' product.id %}" class="bg-purple-500 hover:bg-purple-700 text-white rounded-full p-2 transition duration-300 shadow-md">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">
                    <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
                </svg>
            </a>
            <a href="{% url 'main:delete_product' product.id %}" class="bg-aqua-500 hover:bg-aqua-600 text-black rounded-full p-2 transition duration-300 shadow-md">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
                </svg>
            </a>
        </div>
        </div>

- **Buatlah navigation bar (navbar) untuk fitur-fitur pada aplikasi yang responsive terhadap perbedaan ukuran device, khususnya mobile dan desktop.**
    1. Bagian ini diatur di dalam navbar.html
    2. Berikut kodenya
        <nav class="bg-pink-500 shadow-lg fixed top-0 left-0 z-40 w-screen">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex items-center justify-between h-16">
                <div class="flex items-center">
                <h1 class="text-2xl font-bold text-center text-white">Amolali Bakery</h1>
                </div>
                <!-- Desktop Menu -->
                <div class="hidden md:flex items-center">
                <ul class="flex space-x-7">
                    <li><a href="#" class="text-gray-300 hover:text-white">Home</a></li>
                    <li><a href="#" class="text-gray-300 hover:text-white">Products</a></li>
                    <li><a href="#" class="text-gray-300 hover:text-white">Categories</a></li>
                    <li><a href="#" class="text-gray-300 hover:text-white">Cart</a></li>
                </ul>
                {% if user.is_authenticated %}
                    <span class="text-gray-300 mx-4">Welcome, {{ user.username }}</span>
                    <a href="{% url 'main:logout' %}" class="text-center bg-red-800 hover:bg-red-800 text-white font-bold py-2 px-4 rounded transition duration-300">
                    Logout
                    </a>
                {% else %}
                    <a href="{% url 'main:login' %}" class="text-center bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded transition duration-300 mr-2">
                    Login
                    </a>
                    <a href="{% url 'main:register' %}" class="text-center bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded transition duration-300">
                    Register
                    </a>
                {% endif %}
                </div>
                <div class="md:hidden flex items-center">
                <button class="mobile-menu-button">
                    <svg class="w-6 h-6 text-white" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" stroke="currentColor">
                    <path d="M4 6h16M4 12h16M4 18h16"></path>
                    </svg>
                </button>
                </div>
            </div>
            </div>
            <!-- Mobile menu -->
            <div class="mobile-menu hidden md:hidden px-4 w-full">
            <div class="pt-2 pb-3 space-y-1">
                <a href="#" class="block text-gray-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-base font-medium">Home</a>
                <a href="#" class="block text-gray-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-base font-medium">Products</a>
                <a href="#" class="block text-gray-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-base font-medium">Categories</a>
                <a href="#" class="block text-gray-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-base font-medium">Cart</a>
                {% if user.is_authenticated %}
                <span class="block text-gray-300 px-3 py-2">Welcome, {{ user.username }}</span>
                <a href="{% url 'main:logout' %}" class="block text-center bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded transition duration-300">
                    Logout
                </a>
                {% else %}
                <a href="{% url 'main:login' %}" class="block text-center bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded transition duration-300 mb-2">
                    Login
                </a>
                <a href="{% url 'main:register' %}" class="block text-center bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded transition duration-300">
                    Register
                </a>
                {% endif %}
            </div>
            </div>

            <script>
            const btn = document.querySelector("button.mobile-menu-button");
            const menu = document.querySelector(".mobile-menu");
            
            btn.addEventListener("click", () => {
                menu.classList.toggle("hidden");
            });
            </script>
        </nav>




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

    informasi akun dan last login ada dibagian atas dan bawah
    
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


