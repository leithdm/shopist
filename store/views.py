from django.shortcuts import render, get_object_or_404
from .models import Category, Product

# Create your views here.
def home(request, category_slug=None):
    category_page = None

    # if there is a category slug, filter the home page to show all products of that category
    if category_slug != None:
        category_page = get_object_or_404(Category, slug=category_slug)
        # find all products that belong to a category_page
        products = Product.objects.filter(category=category_page, available=True)
    else:
        # if the category field is empty, display all available products
        products = Product.objects.all().filter(available=True)

    return render(request, 'store/index.html', {'category': category_page, 'products': products})


def productDetails(request):
    return render(request, 'store/product_details.html')