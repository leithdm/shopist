from django.shortcuts import render

# Create your views here.
def store(request):
    return render(request, 'store/index.html')


def productDetails(request):
    return render(request, 'store/product_details.html')