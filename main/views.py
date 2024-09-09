from django.shortcuts import render

def show_main(request):
    blueberry_cheesecake = {
        'name' : 'Blueberry Cheesecake',
        'price': 30000,
        'description': 'Cheesecake lembut creamy dengan topping saus blueberry',
        'category' : 'Dessert'
    }

    return render(request, "main.html", {'blueberry_cheesecake': blueberry_cheesecake})
