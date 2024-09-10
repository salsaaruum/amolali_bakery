from django.shortcuts import render

def show_main(request):
    blueberry_cheesecake = {
        'name' : 'Blueberry Cheesecake',
        'price': 30000,
        'description': 'Cheesecake lembut creamy dengan topping saus blueberry',
        'category' : 'Dessert',
        'image' : 'https://assets.makobakery.com/cdn/web/product_photo/1621578219_blueberry-cheesecake-slice.jpg',
        'space' : '=========================================================================='
    }

    tiramisu = {
        'name' : 'Tiramisu',
        'price': 60000,
        'description': 'Tiramisu degan tekstur yang lembut dan rasa yang menyegarkan, menjadikannya salah satu hidangan penutup favorit',
        'category' : 'Dessert',
        'image' : 'https://nibble-images.b-cdn.net/nibble/original_images/tiramisu_paling_enak_di_jakarta_1_9e8705662b_qhG4omixx.jpg',
        'space' : '=========================================================================='
    }

    croissant = {
        'name' : 'Croissant',
        'price': 25000,
        'description': 'Makanan khas Prancis dengan rasa butter klasik',
        'category' : 'Dessert',
        'image' : 'https://www.aliceboulangerie.com.sg/wp-content/uploads/2023/01/Classic-Croissant--scaled.jpg',
        'space' : '=========================================================================='
    }
    return render(request, "main.html", {'blueberry_cheesecake': blueberry_cheesecake, 'tiramisu': tiramisu, 'croissant': croissant})
