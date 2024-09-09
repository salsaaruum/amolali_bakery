from django.shortcuts import render

def show_main(request):
    blueberry_cheesecake = {
        'name' : 'Blueberry Cheesecake',
        'price': 30000,
        'description': 'Cheesecake lembut creamy dengan topping saus blueberry',
        'category' : 'Dessert',
        'space' : '==============================================================='
    }

    cromboloni = {
        'name' : 'Cromboloni',
        'price': 40000,
        'description': 'Cromboloni yang renyah dengan pilihan isian biscoff, redvelvet, dan pistachio',
        'category' : 'Dessert',
        'space' : '==============================================================='
    }

    croissant = {
        'name' : 'Croissant',
        'price': 25000,
        'description': 'Makanan khas Prancis dengan rasa butter klasik',
        'category' : 'Dessert',
        'space' : '==============================================================='
    }
    return render(request, "main.html", {'blueberry_cheesecake': blueberry_cheesecake, 'cromboloni': cromboloni, 'croissant': croissant})
