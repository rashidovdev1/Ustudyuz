from django.shortcuts import render

# Create your views here.
menu = [{'home':'home', 'about':'about', 'products':'products'}]
about = f"Bu bizning birinchi saytimiz vazifasi mahsulot reklama va sotish"
data = [
    {'id':1,'name':'olma','price':100,'description':'yashil'},
    {'id':2,'name':'gilos','price':200,'description':'qizil'},
    {'id':3,'name':'behi','price':300,'description':'sariq'},
    {'id':4,'name':'banan','price':400,'description':'sariq'},
    {'id':5,'name':'cheri','price':500,'description':'qizil'},
    {'id': 6, 'name': 'nok', 'price': 600, 'description': "ko'k"},
    {'id': 7, 'name': 'qovun', 'price': 700, 'description': 'oq'},
    {'id': 8, 'name': 'tarvuz', 'price': 800, 'description': 'qora'},
]

def get_home(request):
    context = {
        'menu': menu,
    }
    return render(request, 'base.html', context)

def get_about(request):
    context = {
        'about': about,
    }
    return render(request, 'about.html', context)

def get_product(request):
    context = {
        'data': data,
    }
    return render(request, 'product.html', context)