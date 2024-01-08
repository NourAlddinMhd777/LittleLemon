from django.shortcuts import render
from .serializers import MenuSerializer,BookingSerializer
from rest_framework.views import APIView
from .models import Menu,Booking
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateAPIView ,DestroyAPIView 
from rest_framework import generics,viewsets
from rest_framework.decorators import api_view

from . import serializers

# Create your views here.
def index(request):
  return render(request, 'index.html')

class MenuItemView  (generics.ListCreateAPIView):
    queryset =Menu.objects.all()
    serializer_class=MenuSerializer
    def get (self,request):
      items =Menu.objects.all()
      serializer_items = serializers.MenuSerializer(items, many = True)
      return Response(serializer_items.data)
    def post (self , request):
      serializer = MenuSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response({"status":"succsess","data":serializer.data})


class SingleMenuItemView  (RetrieveUpdateAPIView,DestroyAPIView):
  queryset =Menu.objects.all()
  serializer_class=MenuSerializer
  def get (self,request,id):
    items =Menu.objects.get(pk =id )
    serializer = MenuSerializer(items)
    return Response(serializer.data)
  def post (self , request):
    serializer = MenuSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({"status":"succsess","data":serializer.data})
    return Response(serializer.errors, status=400)
  def delete(self , request,id):
        item = Menu.objects.get(pk=id)
        item.delete()
        return Response({"status": "success", "message": "Item deleted."})

class BookingViewSet (viewsets.ModelViewSet):
  queryset =Booking.objects.all()
  serializer_class=BookingSerializer  
  def get (self,request):
    items =Booking.objects.all()
    serializer = BookingSerializer(items, many = True)
    return Response(serializer.data)

