from django.shortcuts import render, redirect

from product.models import Product


# Create your views here.
def get_products(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'product/list.html', context)

def create_product(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        price = request.POST.get('price')
        Product.objects.create(
            title=title,
            description=description,
            price=price)
        return redirect("list")
    return render(request, 'product/create.html')