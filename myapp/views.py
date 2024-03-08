from django.shortcuts import render
from .serializers import MenuSerializer,BookingSerializer
from rest_framework.views import APIView
from .models import Menu,Booking
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateAPIView ,DestroyAPIView 
from rest_framework import viewsets
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated

from . import serializers

# Create your views here.
def index(request):
  return render(request, 'index.html')

class MenuItemView  (ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset =Menu.objects.all()
    serializer_class=MenuSerializer 
    def get (self,request):
      items =Menu.objects.all() 
      #=======================search============================

      search_ID = request.query_params.get("search_by_id")
      if search_ID:
            items= items.filter(id__icontains = search_ID)
      search_Title = request.query_params.get("search_by_title")
      if search_Title:
            items= items.filter(title__icontains = search_Title)
      #=========================================================

      #======================order by===========================
      # ordering by any thing :
      ordering = request.query_params.get("ordering")
      if ordering:
        ordering_fields = ordering.split(",")

        items= items.order_by(*ordering_fields)

      # ordering by price :
      ordering = request.query_params.get("ordering_by_price")
      if ordering == 'True':

        items= items.order_by("price")

      #=============================================
        

      serializer_items = serializers.MenuSerializer(items, many = True)
      return Response(serializer_items.data)
    def post (self ,request):
      serializer = MenuSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response({"status":"succsess","data":serializer.data})


class SingleMenuItemView  (RetrieveUpdateAPIView,DestroyAPIView): #OOOOOOOOOOOOOOO
  permission_classes = [IsAuthenticated] 
  queryset =Menu.objects.all()
  serializer_class=MenuSerializer
  def get (self,request,id):
    items =Menu.objects.get(pk =id )


    serializer = MenuSerializer(items)
    
    return Response(serializer.data)
  def put(self, request,id):
    items =Menu.objects.get(pk =id )
    serializer = MenuSerializer(items,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data})
    return Response(serializer.errors, status=400)
  def delete(self , request,id):
        item = Menu.objects.get(pk=id)
        item.delete()
        return Response({"status": "success", "message": "Item deleted."})

class BookingViewSet (viewsets.ModelViewSet): #OOOOOOOOOOOOOOO
  queryset =Booking.objects.all() 
  serializer_class=BookingSerializer  
  def get (self,request):
    items =Booking.objects.all()
    serializer = BookingSerializer(items, many = True)
    return Response(serializer.data)

