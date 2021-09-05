from .models import Category

'''
Returns a dictionary of all available categores.
This will be used to create Category links on the
store/index.html page
'''


def menu_links(request):
    # return all categories
    links = Category.objects.all()
    return dict(links=links)
