from django.shortcuts import render

# Create your views here.
def store(request):
    return render(request, 'store/index.html')


def aboutPage(request):
    return render(request, 'store/about.html')