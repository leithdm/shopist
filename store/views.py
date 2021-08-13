from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'store/home.html')


def aboutPage(request):
    return render(request, 'store/about.html')