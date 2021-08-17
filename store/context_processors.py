from .models import Category


def menu_links(request):
    #return all categories
    links = Category.objects.all()
    return dict(links=links)