from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator

def index(request):
    products_objects = Product.objects.all()
    item_name = request.GET.get('item_name')
    if item_name!='' and item_name is not None:
        products_objects = products_objects.filter(title__icontains=item_name)
   

    paginator = Paginator(products_objects, 2)
    page = request.GET.get('page', 1)

    # try:
    #     page = p.page(page)
    # except:
    #     page = p.page(1)

    products_objects = paginator.get_page(page)

    context ={
        'items': products_objects
    }
    return render(request, 'shop/index.html', context)