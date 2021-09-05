from django.contrib import admin
from .models import Category, Product, Review


# customize category fields shown on the admin table
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    # pre-populate the slug based on the name field
    prepopulated_fields = {'slug': ('name',)}


# customize product fields shown on the admin table
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'price',
        'stock',
        'available',
        'description',
        'created',
        'updated'
        ]
    list_editable = ['price', 'stock', 'description', 'available']
    prepopulated_fields = {'slug': ('name',)}
    # automate pagination
    list_per_page = 25

# site registration
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Review)
