from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Review
from django.core.paginator import Paginator, EmptyPage, InvalidPage


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

    paginator = Paginator(products, 4)

    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except(EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)

    return render(request, 'store/index.html', {'category': category_page, 'products': products})


def productDetails(request, category_slug, product_slug):
    try:
        product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e

    if request.method == 'POST' and request.user.is_authenticated and request.POST['content'].strip() != '':
        Review.objects.create(product=product,
                              user=request.user,
                              content=request.POST['content'])
    reviews = Review.objects.filter(product=product)    
    return render(request, 'store/product_details.html', {'product': product, 'reviews': reviews})


#ability to search using 'search' field on nav-bar
def search(request):
    products = Product.objects.filter(name__contains=request.GET['product'].lower())
    return render(request, 'store/index.html', {'products': products})