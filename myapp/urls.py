from django.urls import path
from myapp import views
from .views import MenuItemView,SingleMenuItemView,BookingViewSet
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('myapp/', views.index, name='index'),
    path('items/', MenuItemView.as_view(), name='menu_items'),
    path('items/<int:id>', SingleMenuItemView.as_view(), name='single_menu_item'),
    path('api-token-auth/', obtain_auth_token),

]