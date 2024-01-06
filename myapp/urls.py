from django.urls import path

from myapp import views

urlpatterns = [
    path('myapp/', views.index, name='index')
]