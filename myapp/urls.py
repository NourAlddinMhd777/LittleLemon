from django.urls import path
from myapp import views
from .views import MenuItemView,SingleMenuItemView,booking_view

urlpatterns = [
    path('myapp/', views.index, name='index'),
    path('items/', MenuItemView.as_view(), name='menu_items'),
    path('items/<int:id>', SingleMenuItemView.as_view(), name='single_menu_item'),
    path('booking/', booking_view.as_view(), name='booking'),
]