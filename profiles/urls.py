from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order/<int:order_id>', views.viewOrder, name='order_detail'),
    path('delete-review/<int:review_id>', views.deleteReview, name='delete_review'),
]