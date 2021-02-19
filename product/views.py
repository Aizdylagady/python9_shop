from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Category, Product

from django.http import Http404
# Create your views here.


def homepage(request):
    categories = Category.objects.all()
    # SELECT * FROM product_category;
    return render(request, 'Product/index.html', {'categories': categories})


# products? category=slug
# products/category

    # №1
    # products = Product.objects.all()
    # if not Category.objects.filter(slug=category_slug).exists():
    #     raise Http404
    # products = Product.object.filter(category_id=category_slug)
#def products_list(request, category_slug):
    # №2
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category_id=category)

    # №3
    #products = get_list_or_404(Product, category_id=category_slug)  # djangoshortcuts --- get_lost_or_404

    # product = Product.objects.filter(category_id=category_slug)  #QuerySet
    # SELECT * FROM product WHERE category_id = category_slug;
    #return render(request, 'Product/Products_list.html', {'products': products})

# products/?category=slug
# def products_list_2(request):
#     category_slug = request.GET.get('category')
#     products = Product.objects.all()
#     if category_slug is not None:
#         products = products.filter(category_id=category_slug)
#     return render(request, '', {'products': products})


def products(args):
    pass


def products_list(request, category_slug):
    if not Category.objects.filter(slug=category_slug).exists():
        raise Http404('There is no such category')
    products = Product.objects.filter(category_id=category_slug)
    return render(request, 'product/products_list.html', {'products': products})


def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product/product_details.html', {'product':product})


